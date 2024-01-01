from typing import List, Union
import spacy
from nltk.stem import PorterStemmer
from artifician.processors.processor import Processor



class StemLemProcessor(Processor):
    """
    Processor for applying stemming and lemmatization to text data.

    Attributes:
        mode (str): Mode of operation ('stemming' or 'lemmatization').
        nlp: spaCy language model for lemmatization.
        stemmer: NLTK stemmer for stemming.
    """

    def __init__(self, mode: str = 'lemmatization', subscribe_to=None):
        """
        Initialize a StemLemProcessor object.

        Args:
            mode (str): Operation mode ('stemming' or 'lemmatization').
            subscribe_to (list): Optional list of publishers to subscribe to.
        """
        super().__init__()
        if mode not in ['stemming', 'lemmatization']:
            raise ValueError("Invalid mode. Choose 'stemming' or 'lemmatization'.")

        self.mode = mode
        self.nlp = spacy.load("en_core_web_sm") if mode == 'lemmatization' else None
        self.stemmer = PorterStemmer() if mode == 'stemming' else None

        if subscribe_to is not None:
            for publisher in subscribe_to:
                self.subscribe(publisher)

    def process(self, publisher, text: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Process the text or list of tokens for stemming or lemmatization.

        Args:
            publisher: The publisher associated with the processor.
            text (Union[str, List[str]]): The text or list of tokens to be processed.

        Returns:
            Union[str, List[str]]: Processed text or list of processed tokens.
        """
        if text is None or (isinstance(text, list) and not text):
            raise ValueError("Input text cannot be None or an empty list.")

        if isinstance(text, list):
            processed_tokens = [self._process_token(token) for token in text]
            publisher.value = processed_tokens
            return processed_tokens
        else:
            processed_text = ' '.join([self._process_token(token) for token in text.split()])
            publisher.value = processed_text
            return processed_text

    def _process_token(self, token: str) -> str:
        """
        Internal method to apply stemming or lemmatization to a single token.

        Args:
            token (str): The token to be processed.

        Returns:
            str: Processed token.
        """
        if self.mode == 'lemmatization':
            return self.nlp(token)[0].lemma_
        elif self.mode == 'stemming':
            return self.stemmer.stem(token)

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
