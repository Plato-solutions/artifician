from artifician.processors.text.text_cleaner import TextCleaningProcessor

class publisher:
    def __init__(self) -> None:
        self.value = ""
# Test 1: Test Lowercasing
def test_lowercasing():
    pub = publisher()
    processor = TextCleaningProcessor(lowercase=True)
    assert processor.process(pub, "Sample TEXT") == "sample text"

# Test 2: Test Removing Punctuation
def test_remove_punctuation():
    pub = publisher()
    processor = TextCleaningProcessor(remove_punctuation=True)
    assert processor.process(pub, "Hello, world!") == "hello world"

# Test 3: Test Removing Numbers
def test_remove_numbers():
    pub = publisher()
    processor = TextCleaningProcessor(remove_numbers=True)
    assert processor.process(pub, "There are 4 apples") == "there are apples"

# Test 4: Test Stripping Whitespace
def test_strip_whitespace():
    pub = publisher()
    processor = TextCleaningProcessor(strip_whitespace=True)
    assert processor.process(pub, "  Text with spaces  ") == "text with spaces"

# Test 5: Test Removing HTML Tags
def test_remove_html_tags():
    pub = publisher()
    processor = TextCleaningProcessor(remove_html_tags=True)
    assert processor.process(pub, "<p>Some text</p>") == "some text"

# Test 6: Test Removing URLs
def test_remove_urls():
    pub = publisher()
    processor = TextCleaningProcessor(remove_urls=True)
    assert processor.process(pub, "Visit https://example.com") == "visit"

# Test 7: Test List of Strings
def test_list_of_strings():
    pub = publisher()
    processor = TextCleaningProcessor(lowercase=True, remove_punctuation=True)
    assert processor.process(pub, ["Hello, World!", "Sample TEXT"]) == ["hello world", "sample text"]
