"""Number Guessing Game - simple CLI with helper functions and comments.

This module contains:
- check_guess(secret, guess): compares a guess to the secret and returns a short status string
- play_guessing_game(...): main game loop (interactive or demo mode)

The functions are small and easy to test; tests live in `tests/test_number_guessing.py`.
"""
import random
import argparse


def check_guess(secret, guess):
    """Compare the guessed number with the secret.

    Returns:
      - 'correct' if guess == secret
      - 'low' if guess < secret
      - 'high' if guess > secret

    This small helper is perfect for unit tests because it has no I/O.
    """
    if guess == secret:
        return 'correct'
    if guess < secret:
        return 'low'
    return 'high'


def play_guessing_game(max_tries=5, interactive=False):
    """Run the guessing game loop.

    Parameters:
      - max_tries: how many attempts the player gets
      - interactive: if True, read guesses from input(); otherwise run demo mode

    The demo mode makes it easy to show the game without needing keyboard input (useful in notebooks).
    """
    # pick a random secret number between 1 and 50
    secret = random.randint(1, 50)
    tries = 0
    while tries < max_tries:
        tries += 1
        if interactive:
            # Interactive: ask the player to type a number
            guess = int(input(f'Try {tries}/{max_tries} — guess a number (1-50): '))
        else:
            # Demo mode: make a random guess and print it so the demo shows activity
            guess = random.randint(1, 50)
            print(f'Try {tries}: guessed {guess}')

        # Use the helper to get a simple status and act accordingly
        result = check_guess(secret, guess)
        if result == 'correct':
            print('Correct!')
            return True
        elif result == 'low':
            print('Too low')
        else:
            print('Too high')

    # If loop completes without a correct guess, show the secret
    print('Out of tries. Secret was', secret)
    return False


if __name__ == '__main__':
    # Small CLI wrapper to allow demo (--demo) or interactive runs
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true', help='Run demo mode (non-interactive)')
    args = parser.parse_args()
    play_guessing_game(interactive=not args.demo)"
