"""
this is a test file for the corenlp module in the nlplogic package.
"""

from nlplogic import corenlp


def test_get_phrases():
    # Test with a valid Wikipedia page
    phrases = corenlp.get_phrases("Albert Einstein")
    assert isinstance(phrases, list)
    assert len(phrases) > 0

    # Test with an invalid Wikipedia page
    phrases = corenlp.get_phrases("ThisPageDoesNotExist12345")
    assert phrases == []

    # Test with an empty string
    phrases = corenlp.get_phrases("")
    assert phrases == []
