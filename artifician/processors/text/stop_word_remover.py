import spacy
from typing import List, Union
from artifician.processors.processor import Processor

class StopWordsRemoverProcessor(Processor):
    """
    Processor for removing stop words from text data.

    Attributes:
        stop_words (set): A set of stop words to be removed.
    """

    def __init__(self, custom_stop_words: List[str] = None, subscribe_to=None):
        """
        Initialize a StopWordsRemoverProcessor object.

        Args:
            custom_stop_words (List[str]): Optional list of custom stop words.
            subscribe_to (list): Optional list of publishers to subscribe to.
        """
        super().__init__()
        self.nlp = spacy.load("en_core_web_sm")
        self.stop_words = set(self.nlp.Defaults.stop_words)
        
        if custom_stop_words is not None:
            self.stop_words.update(custom_stop_words)

        if subscribe_to is not None:
            for publisher in subscribe_to:
                self.subscribe(publisher)

    def process(self, publisher, text: Union[str, List[str]]) -> Union[str, List[str]]:
        """
        Process the text or list of texts to remove stop words.

        Args:
            publisher: The publisher associated with the processor.
            text (Union[str, List[str]]): The text or list of texts to be processed.

        Returns:
            Union[str, List[str]]: Text after stop words removal.

        Raises:
            ValueError: If the input text is None or an empty list.
        """
        if text is None or (isinstance(text, list) and not text):
            raise ValueError("Input text cannot be None or an empty list.")

        if isinstance(text, list):
            processed_output = [word for word in text if word.lower() not in self.stop_words]
        else:
            processed_output = ' '.join(word for word in text.split() if word.lower() not in self.stop_words)

        publisher.value = processed_output
        return processed_output

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
