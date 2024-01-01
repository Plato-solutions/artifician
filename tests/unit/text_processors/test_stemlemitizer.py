from artifician.processors.text.stemlemtizer import StemLemProcessor
import pytest
class publisher:
    def __init__(self) -> None:
        self.value = ""

class TestStemlemitizer:
    def test_lemmatization(self):
        processor = StemLemProcessor(mode='lemmatization')
        pub = publisher()
        result = processor.process(pub, "The cats are running")
        assert result == "the cat be run"

    # Test 2: Test Stemming
    def test_stemming(self):
        processor = StemLemProcessor(mode='stemming')
        pub = publisher()
        result = processor.process(pub, "The cats are running")
        assert result == "the cat are run"

    # Test 3: Test None Input
    def test_none_input(self):
        processor = StemLemProcessor(mode='lemmatization')
        with pytest.raises(ValueError):
            processor.process(None, None)

    # Test 4: Test Empty String
    def test_empty_string(self):
        processor = StemLemProcessor(mode='lemmatization')
        pub = publisher()
        result = processor.process(pub, "")
        assert result == ""

    # Test 6: Test Invalid Mode
    def test_invalid_mode(self):
        with pytest.raises(ValueError):
            StemLemProcessor(mode='invalid')

    # Test 7: Test Single Word Lemmatization
    def test_single_word_lemmatization(self):
        processor = StemLemProcessor(mode='lemmatization')
        pub = publisher()
        result = processor.process(pub, "running")
        assert result == "run"

    # Test 8: Test Single Word Stemming
    def test_single_word_stemming(self):
        processor = StemLemProcessor(mode='stemming')
        pub = publisher()
        result = processor.process(pub, "running")
        assert result == "run"