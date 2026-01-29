# Tests for calculator.safe_eval - check basic arithmetic and precedence
from interview_projects.calculator.calculator import safe_eval


def test_basic_calculations():
    assert safe_eval('2+3') == 5
    # multiplication has higher precedence than addition
    assert safe_eval('2 + 3 * 4') == 14
    # unary minus should work
    assert safe_eval('-5 + 2') == -3
