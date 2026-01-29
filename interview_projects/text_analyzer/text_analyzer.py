"""Text Analyzer - count words and characters and find most common words.

This script demonstrates text processing and the use of `collections.Counter` to aggregate counts.
"""
import sys
from collections import Counter


def analyze_text(text):
    """Analyze the input text and return counts and top words.

    Returns a dict with keys: words, chars, top_words (list), word_counts (dict)
    """
    # Normalize words to lowercase and split on whitespace
    words = text.lower().split()
    word_counts = Counter(words)
    char_count = len(text)
    return {
        'words': len(words),
        'chars': char_count,
        'top_words': word_counts.most_common(5),
        'word_counts': dict(word_counts)
    }


if __name__ == '__main__':
    # CLI demo: read a file path or use sample_text.txt
    path = sys.argv[1] if len(sys.argv) > 1 else 'sample_text.txt'
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    result = analyze_text(text)
    print('Words:', result['words'])
    print('Chars:', result['chars'])
    print('Top words:', result['top_words'])
