import re
from artifician.processors.processor import Processor
from typing import List, Union

class TextCleaningProcessor(Processor):
    """
    Processor for cleaning and preprocessing text data.

    Configurable attributes for various cleaning operations.
    """

    def __init__(self, lowercase=True, remove_punctuation=True, remove_numbers=True, 
                 strip_whitespace=True, remove_html_tags=True, remove_urls=True, 
                 subscribe_to=None):
        """
        Initialize a TextCleaningProcessor object.

        Args:
            lowercase (bool): Flag to convert text to lowercase.
            remove_punctuation (bool): Flag to remove punctuation.
            remove_numbers (bool): Flag to remove numbers.
            strip_whitespace (bool): Flag to strip extra whitespaces.
            remove_html_tags (bool): Flag to remove HTML tags.
            remove_urls (bool): Flag to remove URLs.
            custom_stop_words (List[str]): Optional list of custom stop words.
            subscribe_to (list): Optional list of publishers to subscribe to.
        """
        super().__init__()
        self.lowercase = lowercase
        self.remove_punctuation = remove_punctuation
        self.remove_numbers = remove_numbers
        self.strip_whitespace = strip_whitespace
        self.remove_html_tags = remove_html_tags
        self.remove_urls = remove_urls

        if subscribe_to is not None:
            for publisher in subscribe_to:
                self.subscribe(publisher)

    def process(self, publisher, text: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Process the text or list of texts to clean and preprocess.

        Args:
            publisher: The publisher associated with the processor.
            text (Union[str, List[str]]): The text or list of texts to be processed.

        Returns:
            Union[str, List[str]]: Cleaned and preprocessed text.
        """
        if text is None or (isinstance(text, list) and not text):
            raise ValueError("Input text cannot be None or an empty list.")

        processed_output = [self._clean_text(t) for t in text] if isinstance(text, list) else self._clean_text(text)
        publisher.value = processed_output
        return processed_output

    def _clean_text(self, text: str) -> str:
        """
        Internal method to apply configured cleaning operations to a single text string.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: Cleaned text.
        """
        if self.lowercase:
            text = text.lower()
        if self.remove_urls:
            text = re.sub(r'https?://\S+|www\.\S+', '', text)
        if self.remove_html_tags:
            text = re.sub(r'<.*?>', '', text)
        if self.remove_punctuation:
            text = re.sub(r'[^\w\s]', '', text)
        if self.remove_numbers:
            text = re.sub(r'\d+', '', text)
        if self.strip_whitespace:
            text = text.strip()
            text = re.sub(r'\s+', ' ', text)
        return text


    def subscribe(self, publisher, pool_scheduler=None):
        """
        Subscribe to a publisher for event-driven processing.

        Args:
            publisher (object): The publisher to subscribe to.
            pool_scheduler (optional): Scheduler instance for concurrency.

        Returns:
            None
        """
        observable = publisher.observe(publisher.EVENT_PROCESSED)
        observable.subscribe(lambda value: self.process(publisher, value),
                             scheduler=pool_scheduler)
