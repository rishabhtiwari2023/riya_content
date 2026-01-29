"""Calculator: safely evaluate simple arithmetic expressions using `ast`.

This module avoids `eval()` and instead parses the expression into an AST and evaluates
only a small set of safe nodes (numbers, binary ops, unary ops). This is a good
example to discuss in an interview when explaining why `eval` is dangerous and how
we can implement safe parsing for simple languages.
"""
import ast
import operator as op
import sys

# Mapping from AST operator node types to actual Python operator functions
OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg
}


def safe_eval(expr):
    """Parse the expression into an AST and evaluate only allowed nodes.

    Raises TypeError on unsupported node types to prevent code execution.
    """
    node = ast.parse(expr, mode='eval')
    return _eval(node.body)


def _eval(node):
    # Number literal
    if isinstance(node, ast.Num):
        return node.n
    # Binary operation: evaluate left and right recursively then apply operator
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        return OPERATORS[type(node.op)](left, right)
    # Unary operation (like negative numbers)
    if isinstance(node, ast.UnaryOp):
        return OPERATORS[type(node.op)](_eval(node.operand))
    # Any other node type is rejected for safety
    raise TypeError('Unsupported expression')


if __name__ == '__main__':
    expr = sys.argv[1] if len(sys.argv) > 1 else '2 + 3 * (4 - 1)'
    print('Expr:', expr)
    print('Result:', safe_eval(expr))
