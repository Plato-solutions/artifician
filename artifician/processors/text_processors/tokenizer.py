from artifician.processors.processor import Processor
import spacy
from typing import List, Union
class TokenizationProcessor(Processor):
    """
    Tokenization Processor for splitting text into tokens.

    Attributes:
        method (str): Method to use for tokenization ('word' or 'sentence').
        nlp: spaCy language model for processing text.
    """


    def __init__(self, method: str = 'word', subscribe_to=None):
        """
        Initialize a TokenizationProcessor object.

        Args:
            method (str): Method to use for tokenization ('word' or 'sentence').
        """
        super().__init__()
        if method not in ['word', 'sentence']:
            raise ValueError("Invalid tokenization method. Choose 'word' or 'sentence'.")

        self.method = method
        self.nlp = spacy.load("en_core_web_sm")

        if subscribe_to is not None:
            for publisher in subscribe_to:
                self.subscribe(publisher)

    def process(self, publisher, text: Union[str, List[str], None]) -> Union[List[str], List[List[str]]]:
        """
        Process the text or list of texts and split it into tokens.

        Args:
            text (Union[str, List[str], None]): The text or list of texts to be tokenized.

        Returns:
            Union[List[str], List[List[str]]]: A list of tokens or list of lists of tokens.

        Raises:
            ValueError: If the input text is None or an empty list.
        """
        if text is None or (isinstance(text, list) and not text):
            raise ValueError("Input text cannot be None or an empty list for tokenization.")

        if isinstance(text, list):
            publisher.value = [self._tokenize(t) for t in text]
            return publisher.value
        else:
            return self._tokenize(text)

    def _tokenize(self, text: str) -> List[str]:
        """
        Internal method to tokenize a single text string.

        Args:
            text (str): The text to be tokenized.

        Returns:
            List[str]: A list of tokens.
        """
        if self.method == 'word':
            return [token.text for token in self.nlp(text)]
        elif self.method == 'sentence':
            return [sent.text.strip() for sent in self.nlp(text).sents]

        raise ValueError(f"Unknown tokenization method: {self.method}")
    
    def subscribe(self, publisher, pool_scheduler=None):
        """Defines logic for subscribing to an event in publisher

        Args:
            publisher (object): instance of the publisher
            pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

        Returns:
            None
        """
        observable = publisher.observe(publisher.EVENT_PROCESSED)
        observable = observable.subscribe(lambda value: self.process(publisher, value),
                                          scheduler=pool_scheduler)