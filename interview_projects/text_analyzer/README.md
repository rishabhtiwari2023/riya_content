# Text Analyzer

A small script to analyze text: count words, count characters, and find the most common words. Good demo of strings, dictionaries, and basic file handling.

How to run:
- `python text_analyzer.py sample_text.txt`

Presentation script:
- Elevator pitch: "This reads a text file, computes word frequencies, top words, and basic stats (word and character count)."
- Show example output and explain how dictionaries are used to aggregate counts.
- Extension ideas: ignore stopwords, add plotting, or read multiple files.

File guide:
- `text_analyzer.py` — `analyze_text(text)` returns word/char counts and top words using `collections.Counter`.
- `sample_text.txt` — a small sample text file for demo runs.
- `tests/test_text_analyzer.py` — unit tests verifying the analyzer outputs expected counts.

Tips for interview: show the top words output and explain how `Counter` makes it easy to get frequencies and top items.
