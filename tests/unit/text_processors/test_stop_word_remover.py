import pytest
from artifician.processors.text.stop_word_remover import StopWordsRemoverProcessor


class publisher:
    def __init__(self) -> None:
        self.value = ""
# Test 1: Test Stop Word Removal with Single String
def test_stop_word_removal_single_string():
    processor = StopWordsRemoverProcessor()
    pub = publisher()
    result = processor.process(pub, "This is a test")
    assert result == "test"

# Test 2: Test None Input
def test_none_input():
    processor = StopWordsRemoverProcessor()
    pub = publisher()
    with pytest.raises(ValueError):
        processor.process(pub, None)

# Test 3: Test Empty String
def test_empty_string():
    processor = StopWordsRemoverProcessor()
    pub = publisher()
    result = processor.process(pub, "")
    assert result == ""

# Test 5: Test Custom Stop Words
def test_custom_stop_words():
    custom_stop_words = ["sample"]
    pub = publisher()
    processor = StopWordsRemoverProcessor(custom_stop_words=custom_stop_words)
    result = processor.process(pub, "This is a sample text")
    assert result == "text"

# Test 6: Test Single Word
def test_single_word():
    processor = StopWordsRemoverProcessor()
    pub = publisher()
    result = processor.process(pub, "sample")
    assert result == "sample"