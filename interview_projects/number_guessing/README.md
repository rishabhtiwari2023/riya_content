# Number Guessing Game

A small CLI game where the player guesses a secret number. Good demo of control flow, randomness, and simple I/O.

Features:
- Random secret number generation
- Limited tries and friendly feedback (too low / too high)
- Option to play interactively or run demo mode

How to run:
- Interactive: `python number_guessing.py` and follow prompts
- Demo: `python number_guessing.py --demo` or run the file in a notebook

Presentation script:
- Elevator pitch: "This is a simple game that chooses a secret number and gives the player hints until they guess it or run out of tries."
- Show the code for `play_guessing_game` and explain the loop and conditions
- Talk about a possible extension (save high-scores to CSV, add difficulty levels)

File guide:
- `number_guessing.py` — Contains `check_guess(secret, guess)` and `play_guessing_game()`; the first is a pure function (easy to test), the second is the game loop (interactive/demo modes).
- `tests/test_number_guessing.py` — Unit tests for `check_guess` to show basic testing knowledge and keep the game logic verifiable.

Tips for interview: open `number_guessing.py`, point to the small pure function and the small game loop, and mention how tests make it easier to maintain and extend.
