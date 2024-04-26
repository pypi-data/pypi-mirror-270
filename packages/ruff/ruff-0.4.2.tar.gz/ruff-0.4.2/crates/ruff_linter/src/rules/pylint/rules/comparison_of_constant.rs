use itertools::Itertools;
use ruff_python_ast::{CmpOp, Expr};

use ruff_diagnostics::{Diagnostic, Violation};
use ruff_macros::{derive_message_formats, violation};
use ruff_text_size::Ranged;

use crate::checkers::ast::Checker;
use crate::rules::pylint::helpers::CmpOpExt;

/// ## What it does
/// Checks for comparisons between constants.
///
/// ## Why is this bad?
/// Comparing two constants will always resolve to the same value, so the
/// comparison is redundant. Instead, the expression should be replaced
/// with the result of the comparison.
///
/// ## Example
/// ```python
/// foo = 1 == 1
/// ```
///
/// Use instead:
/// ```python
/// foo = True
/// ```
///
/// ## References
/// - [Python documentation: Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons)
#[violation]
pub struct ComparisonOfConstant {
    left_constant: String,
    op: CmpOp,
    right_constant: String,
}

impl Violation for ComparisonOfConstant {
    #[derive_message_formats]
    fn message(&self) -> String {
        let ComparisonOfConstant {
            left_constant,
            op,
            right_constant,
        } = self;

        format!(
            "Two constants compared in a comparison, consider replacing `{left_constant} {} {right_constant}`",
            CmpOpExt::from(op)
        )
    }
}

/// PLR0133
pub(crate) fn comparison_of_constant(
    checker: &mut Checker,
    left: &Expr,
    ops: &[CmpOp],
    comparators: &[Expr],
) {
    for ((left, right), op) in std::iter::once(left)
        .chain(comparators.iter())
        .tuple_windows()
        .zip(ops)
    {
        if left.is_literal_expr() && right.is_literal_expr() {
            let diagnostic = Diagnostic::new(
                ComparisonOfConstant {
                    left_constant: checker.generator().expr(left),
                    op: *op,
                    right_constant: checker.generator().expr(right),
                },
                left.range(),
            );

            checker.diagnostics.push(diagnostic);
        };
    }
}
