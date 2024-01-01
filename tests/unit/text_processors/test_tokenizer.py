import pytest
from artifician.processors.text.tokenizer import TokenizationProcessor

# Test 1: Test Word Tokenization

class publisher:
    def __init__(self) -> None:
        self.value = ""
class TestTokenizationProcessor:
    def test_word_tokenization(self,):
        tokenizer = TokenizationProcessor(method='word')
        pub = publisher()
        result = tokenizer.process(pub, "Hello world!")
        assert result == ["Hello", "world", "!"]

    # Test 2: Test Sentence Tokenization
    def test_sentence_tokenization(self):
        tokenizer = TokenizationProcessor(method='sentence')
        pub = publisher()
        result = tokenizer.process(pub,"Hello world! This is a test.")
        assert result == ["Hello world!", "This is a test."]

    # Test 3: Test None Input
    def test_none_input(self):
        tokenizer = TokenizationProcessor(method='word')
        with pytest.raises(ValueError):
            tokenizer.process(None, None)

    # Test 4: Test Empty String
    def test_empty_string(self):
        tokenizer = TokenizationProcessor(method='word')
        pub = publisher()
        result = tokenizer.process(pub,"")
        assert result == []

    # Test 5: Test List of Strings Input for Word Tokenization
    def test_list_of_strings_word_tokenization(self):
        tokenizer = TokenizationProcessor(method='word')
        pub = publisher()
        result = tokenizer.process(pub, ["Hello world!", "This is a test."])
        assert result == [["Hello", "world", "!"], ["This", "is", "a", "test", "."]]

    # Test 6: Test Invalid Tokenization Method
    def test_invalid_tokenization_method(self):
        with pytest.raises(ValueError):
            TokenizationProcessor(method='invalid')

    # Test 7: Test Punctuation Handling in Word Tokenization
    def test_punctuation_handling_word_tokenization(self):
        tokenizer = TokenizationProcessor(method='word')
        pub = publisher()
        result = tokenizer.process(pub,"Hello, world!")
        assert result == ["Hello", ",", "world", "!"]

    # Test 8: Test Multiple Sentences in Sentence Tokenization
    def test_multiple_sentences_sentence_tokenization(self):
        tokenizer = TokenizationProcessor(method='sentence')
        pub = publisher()
        result = tokenizer.process(pub,"Hello world! This is a test. Another sentence.")
        assert result == ["Hello world!", "This is a test.", "Another sentence."]