# Tests for number_guessing.check_guess
# These tests focus on the pure helper function (no I/O), which makes them easy to run and explain.
from interview_projects.number_guessing.number_guessing import check_guess


def test_check_guess_correct():
    # equal values -> 'correct'
    assert check_guess(10, 10) == 'correct'


def test_check_guess_low():
    # guess less than secret -> 'low'
    assert check_guess(10, 5) == 'low'


def test_check_guess_high():
    # guess greater than secret -> 'high'
    assert check_guess(10, 20) == 'high'
