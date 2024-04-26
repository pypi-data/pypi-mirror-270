use crate::line_width::IndentWidth;
use ruff_diagnostics::Diagnostic;
use ruff_python_codegen::Stylist;
use ruff_python_index::Indexer;
use ruff_python_parser::lexer::LexResult;
use ruff_python_parser::TokenKind;
use ruff_source_file::Locator;
use ruff_text_size::{Ranged, TextRange};

use crate::registry::AsRule;
use crate::rules::pycodestyle::rules::logical_lines::{
    extraneous_whitespace, indentation, missing_whitespace, missing_whitespace_after_keyword,
    missing_whitespace_around_operator, redundant_backslash, space_after_comma,
    space_around_operator, whitespace_around_keywords, whitespace_around_named_parameter_equals,
    whitespace_before_comment, whitespace_before_parameters, LogicalLines, TokenFlags,
};
use crate::settings::LinterSettings;

/// Return the amount of indentation, expanding tabs to the next multiple of the settings' tab size.
pub(crate) fn expand_indent(line: &str, indent_width: IndentWidth) -> usize {
    let line = line.trim_end_matches(['\n', '\r']);

    let mut indent = 0;
    let tab_size = indent_width.as_usize();
    for c in line.bytes() {
        match c {
            b'\t' => indent = (indent / tab_size) * tab_size + tab_size,
            b' ' => indent += 1,
            _ => break,
        }
    }

    indent
}

pub(crate) fn check_logical_lines(
    tokens: &[LexResult],
    locator: &Locator,
    indexer: &Indexer,
    stylist: &Stylist,
    settings: &LinterSettings,
) -> Vec<Diagnostic> {
    let mut context = LogicalLinesContext::new(settings);

    let mut prev_line = None;
    let mut prev_indent_level = None;
    let indent_char = stylist.indentation().as_char();

    for line in &LogicalLines::from_tokens(tokens, locator) {
        if line.flags().contains(TokenFlags::OPERATOR) {
            space_around_operator(&line, &mut context);
            whitespace_around_named_parameter_equals(&line, &mut context);
            missing_whitespace_around_operator(&line, &mut context);
            missing_whitespace(&line, &mut context);
        }
        if line.flags().contains(TokenFlags::PUNCTUATION) {
            space_after_comma(&line, &mut context);
        }

        if line
            .flags()
            .intersects(TokenFlags::OPERATOR | TokenFlags::BRACKET | TokenFlags::PUNCTUATION)
        {
            extraneous_whitespace(&line, &mut context);
        }

        if line.flags().contains(TokenFlags::KEYWORD) {
            whitespace_around_keywords(&line, &mut context);
            missing_whitespace_after_keyword(&line, &mut context);
        }

        if line.flags().contains(TokenFlags::COMMENT) {
            whitespace_before_comment(&line, locator, &mut context);
        }

        if line.flags().contains(TokenFlags::BRACKET) {
            whitespace_before_parameters(&line, &mut context);
            redundant_backslash(&line, locator, indexer, &mut context);
        }

        // Extract the indentation level.
        let Some(first_token) = line.first_token() else {
            continue;
        };

        let range = if first_token.kind() == TokenKind::Indent {
            first_token.range()
        } else {
            TextRange::new(locator.line_start(first_token.start()), first_token.start())
        };

        let indent_level = expand_indent(locator.slice(range), settings.tab_size);

        let indent_size = 4;

        for kind in indentation(
            &line,
            prev_line.as_ref(),
            indent_char,
            indent_level,
            prev_indent_level,
            indent_size,
        ) {
            if settings.rules.enabled(kind.rule()) {
                context.push_diagnostic(Diagnostic::new(kind, range));
            }
        }

        if !line.is_comment_only() {
            prev_line = Some(line);
            prev_indent_level = Some(indent_level);
        }
    }
    context.diagnostics
}

#[derive(Debug, Clone)]
pub(crate) struct LogicalLinesContext<'a> {
    settings: &'a LinterSettings,
    diagnostics: Vec<Diagnostic>,
}

impl<'a> LogicalLinesContext<'a> {
    fn new(settings: &'a LinterSettings) -> Self {
        Self {
            settings,
            diagnostics: Vec::new(),
        }
    }

    pub(crate) fn push_diagnostic(&mut self, diagnostic: Diagnostic) {
        if self.settings.rules.enabled(diagnostic.kind.rule()) {
            self.diagnostics.push(diagnostic);
        }
    }
}
