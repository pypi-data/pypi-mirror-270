use ruff_python_ast::{self as ast, ExceptHandler, Expr, ExprContext};
use ruff_text_size::{Ranged, TextRange};

use crate::fix::edits::pad;
use ruff_diagnostics::{AlwaysFixableViolation, Diagnostic, Edit, Fix};
use ruff_macros::{derive_message_formats, violation};
use ruff_python_ast::name::UnqualifiedName;
use ruff_python_semantic::SemanticModel;

use crate::checkers::ast::Checker;

/// ## What it does
/// Checks for uses of exceptions that alias `OSError`.
///
/// ## Why is this bad?
/// `OSError` is the builtin error type used for exceptions that relate to the
/// operating system.
///
/// In Python 3.3, a variety of other exceptions, like `WindowsError` were
/// aliased to `OSError`. These aliases remain in place for compatibility with
/// older versions of Python, but may be removed in future versions.
///
/// Prefer using `OSError` directly, as it is more idiomatic and future-proof.
///
/// ## Example
/// ```python
/// raise IOError
/// ```
///
/// Use instead:
/// ```python
/// raise OSError
/// ```
///
/// ## References
/// - [Python documentation: `OSError`](https://docs.python.org/3/library/exceptions.html#OSError)
#[violation]
pub struct OSErrorAlias {
    name: Option<String>,
}

impl AlwaysFixableViolation for OSErrorAlias {
    #[derive_message_formats]
    fn message(&self) -> String {
        format!("Replace aliased errors with `OSError`")
    }

    fn fix_title(&self) -> String {
        let OSErrorAlias { name } = self;
        match name {
            None => "Replace with builtin `OSError`".to_string(),
            Some(name) => format!("Replace `{name}` with builtin `OSError`"),
        }
    }
}

/// Return `true` if an [`Expr`] is an alias of `OSError`.
fn is_alias(expr: &Expr, semantic: &SemanticModel) -> bool {
    semantic
        .resolve_qualified_name(expr)
        .is_some_and(|qualified_name| {
            matches!(
                qualified_name.segments(),
                [
                    "" | "builtins",
                    "EnvironmentError" | "IOError" | "WindowsError"
                ] | ["mmap" | "select" | "socket" | "os", "error"]
            )
        })
}

/// Create a [`Diagnostic`] for a single target, like an [`Expr::Name`].
fn atom_diagnostic(checker: &mut Checker, target: &Expr) {
    let mut diagnostic = Diagnostic::new(
        OSErrorAlias {
            name: UnqualifiedName::from_expr(target).map(|name| name.to_string()),
        },
        target.range(),
    );
    diagnostic.try_set_fix(|| {
        let (import_edit, binding) = checker.importer().get_or_import_builtin_symbol(
            "OSError",
            target.start(),
            checker.semantic(),
        )?;
        Ok(Fix::safe_edits(
            Edit::range_replacement(binding, target.range()),
            import_edit,
        ))
    });
    checker.diagnostics.push(diagnostic);
}

/// Create a [`Diagnostic`] for a tuple of expressions.
fn tuple_diagnostic(checker: &mut Checker, tuple: &ast::ExprTuple, aliases: &[&Expr]) {
    let mut diagnostic = Diagnostic::new(OSErrorAlias { name: None }, tuple.range());
    let semantic = checker.semantic();
    if semantic.has_builtin_binding("OSError") {
        // Filter out any `OSErrors` aliases.
        let mut remaining: Vec<Expr> = tuple
            .elts
            .iter()
            .filter_map(|elt| {
                if aliases.contains(&elt) {
                    None
                } else {
                    Some(elt.clone())
                }
            })
            .collect();

        // If `OSError` itself isn't already in the tuple, add it.
        if tuple
            .elts
            .iter()
            .all(|elt| !semantic.match_builtin_expr(elt, "OSError"))
        {
            let node = ast::ExprName {
                id: "OSError".into(),
                ctx: ExprContext::Load,
                range: TextRange::default(),
            };
            remaining.insert(0, node.into());
        }

        let content = if remaining.len() == 1 {
            "OSError".to_string()
        } else {
            let node = ast::ExprTuple {
                elts: remaining,
                ctx: ExprContext::Load,
                range: TextRange::default(),
                parenthesized: true,
            };
            format!("({})", checker.generator().expr(&node.into()))
        };

        diagnostic.set_fix(Fix::safe_edit(Edit::range_replacement(
            pad(content, tuple.range(), checker.locator()),
            tuple.range(),
        )));
    }
    checker.diagnostics.push(diagnostic);
}

/// UP024
pub(crate) fn os_error_alias_handlers(checker: &mut Checker, handlers: &[ExceptHandler]) {
    for handler in handlers {
        let ExceptHandler::ExceptHandler(ast::ExceptHandlerExceptHandler { type_, .. }) = handler;
        let Some(expr) = type_.as_ref() else {
            continue;
        };
        match expr.as_ref() {
            Expr::Name(_) | Expr::Attribute(_) => {
                if is_alias(expr, checker.semantic()) {
                    atom_diagnostic(checker, expr);
                }
            }
            Expr::Tuple(tuple) => {
                // List of aliases to replace with `OSError`.
                let mut aliases: Vec<&Expr> = vec![];
                for elt in &tuple.elts {
                    if is_alias(elt, checker.semantic()) {
                        aliases.push(elt);
                    }
                }
                if !aliases.is_empty() {
                    tuple_diagnostic(checker, tuple, &aliases);
                }
            }
            _ => {}
        }
    }
}

/// UP024
pub(crate) fn os_error_alias_call(checker: &mut Checker, func: &Expr) {
    if is_alias(func, checker.semantic()) {
        atom_diagnostic(checker, func);
    }
}

/// UP024
pub(crate) fn os_error_alias_raise(checker: &mut Checker, expr: &Expr) {
    if matches!(expr, Expr::Name(_) | Expr::Attribute(_)) {
        if is_alias(expr, checker.semantic()) {
            atom_diagnostic(checker, expr);
        }
    }
}
