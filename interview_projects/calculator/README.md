# Calculator CLI

A small command-line calculator that safely evaluates arithmetic expressions. Good demo of parsing, `ast` usage for safety, and small tests.

How to run:
- `python calculator.py "2 + 3 * (4 - 1)"`

Presentation script:
- Elevator pitch: "A safe calculator that evaluates arithmetic expressions while preventing execution of arbitrary code."
- Explain why `eval` is dangerous and how `ast` can be used to parse and evaluate expressions safely.
- Extension ideas: add variables, history, or a simple GUI.

File guide:
- `calculator.py` — implements `safe_eval(expr)` which parses expressions and evaluates only safe AST nodes (numbers, binary/unary ops).
- `tests/test_calculator.py` — tests that verify operator precedence, unary minus and simple arithmetic.

Tips for interview: explain why you avoid `eval`, show the AST `_eval` function and mention how to extend supported operators safely.
