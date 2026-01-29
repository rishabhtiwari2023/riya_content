# Tests for text_analyzer.analyze_text
# The tests check basic word/character counts and expected behavior of returned structures
from interview_projects.text_analyzer.text_analyzer import analyze_text


def test_analyze_text():
    text = 'a a b c'
    res = analyze_text(text)
    # Expect 4 words total
    assert res['words'] == 4
    # 'a' appears twice
    assert res['word_counts']['a'] == 2
    # top_words should be a list of (word, count) tuples
    assert isinstance(res['top_words'], list)
