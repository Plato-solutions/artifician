from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from typing import List, Union, Optional
import logging
import spacy

logging.basicConfig(level=logging.INFO)
class KeywordExtractor:
    """
    Keyword Extractor class for extracting specific keywords from a text.

    Attributes:
        method (str): Method to use for keyword extraction ('manual', 'frequency', 'tfidf', etc.)
        keywords (List[str]): List of keywords to search within the text for 'manual' method.
    """

    def __init__(self, method: str = 'manual', keywords: List[str] = None):
        """
        Initialize a new KeywordExtractor object.

        Args:
            method (str): Method to use for keyword extraction.
            keywords (List[str]): List of keywords to search within the text for 'manual' method.

        Raises:
            ValueError: If the keywords list is empty for 'manual' method.
        """
        self.method = method
        if self.method == 'manual' and not keywords:
            raise ValueError("Keywords list cannot be empty for 'manual' method.")
        
        self.keywords = keywords if self.method == 'manual' else None
        self.nlp = spacy.load("en_core_web_sm")  # Load English tokenizer, POS tagger, NER, etc.

    def extract(self, text: Union[str, None], corpus: List[str] = None) -> List[str]:
        if text is None:
            raise ValueError("Input text cannot be None.")

        if self.method == 'manual':
            return self._manual_extract(text)
        elif self.method == 'frequency':
            return self._frequency_extract(text)
        elif self.method == 'tfidf':
            if corpus is None:
                raise ValueError("Corpus can't be None for 'tfidf' method.")
            return self._tfidf_extract(text, corpus)
        elif self.method == 'ngram':
            return self._ngram_extract(text)
        elif self.method == 'ner':
            return self._ner_extract(text)
        elif self.method == 'pos':
            return self._pos_extract(text)
        else:
            raise ValueError(f"Unknown method {self.method}")

    def _manual_extract(self, text: str) -> List[str]:
        """
        Manually extract keywords based on a pre-defined list.

        Args:
            text (str): The text to extract keywords from.

        Returns:
            List[str]: Extracted keywords that match the list.
        """
        return [word for word in self.keywords if word in text]

    def _frequency_extract(self, text: str, min_frequency: int = 2) -> List[str]:
        """
        Extract keywords based on frequency.

        Args:
            text (str): The text to extract keywords from.
            min_frequency (int): Minimum frequency for a word to be considered a keyword.

        Returns:
            List[str]: Extracted keywords based on frequency.
        """
        words = text.split()
        word_freq = Counter(words)
        return [word for word, freq in word_freq.items() if freq >= min_frequency]

    def _tfidf_extract(self, text: str, corpus: List[str]) -> List[str]:
        """
        Extract keywords using TF-IDF.

        Args:
            text (str): The text to extract keywords from.
            corpus (List[str]): The collection of documents to fit the TF-IDF model.

        Returns:
            List[str]: Extracted keywords based on TF-IDF scores.
        """
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(corpus)
        feature_names = vectorizer.get_feature_names_out()
        tfidf_vector = vectorizer.transform([text])
        sorted_items = self._sort_coo(tfidf_vector.tocoo())
        keywords = self._extract_topn_from_vector(feature_names, sorted_items, 10)
        return keywords

    @staticmethod
    def _sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    @staticmethod
    def _extract_topn_from_vector(feature_names, sorted_items, topn=10):
        """return n-gram list with highest tf-idf."""

        # use only topn items from vector
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        for idx, score in sorted_items:
            fname = feature_names[idx]
            
            # keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])

        results = {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]] = score_vals[idx]
        
        return results

    def _ngram_extract(self, text: str, n=2) -> List[str]:
        """
        Extract n-grams from the text.

        Args:
            text (str): The text to extract n-grams from.
            n (int): The 'n' in n-grams, representing the number of grouped words.

        Returns:
            List[str]: Extracted n-grams.
        """
        words = text.split()
        ngrams = zip(*[words[i:] for i in range(n)])
        return [" ".join(ngram) for ngram in ngrams]
    
    def _ner_extract(self, text: str) -> List[str]:
        """
        Perform Named Entity Recognition (NER) to extract keywords.

        This method uses NER to identify and extract named entities such as names of people,
        organizations, locations, etc., from the given text.

        Args:
            text (str): The text from which to extract named entities.

        Returns:
            List[str]: A list of extracted named entities.

        Raises:
            Exception: If any error occurs during the extraction process.
        """
        try:
            doc = self.nlp(text)
            if not doc.ents:
                logging.warning("No named entities found in the text.")
                return []
            extracted_entities = [ent.text for ent in doc.ents]
            logging.info(f"NER extraction found {len(extracted_entities)} keywords.")
            return extracted_entities
        except Exception as e:
            logging.error(f"An error occurred during NER extraction: {e}")
            return []

    def _pos_extract(self, text: str, pos_tags: Optional[List[str]] = None) -> List[str]:
        """
        Extract keywords based on Part-of-Speech (POS) tagging.

        This method uses POS tagging to identify and extract specific types of words,
        such as nouns, proper nouns, and verbs, from the given text.

        Args:
            text (str): The text from which to extract words based on their POS tags.
            pos_tags (Optional[List[str]]): A list of POS tags to consider for extraction. 
                                            Defaults to ["NOUN", "PROPN", "VERB"].

        Returns:
            List[str]: A list of extracted words based on their POS tags.

        Raises:
            Exception: If any error occurs during the extraction process.
        """
        if pos_tags is None:
            pos_tags = ["NOUN", "PROPN", "VERB"]

        try:
            doc = self.nlp(text)
            extracted_words = [token.text for token in doc if token.pos_ in pos_tags]
            if not extracted_words:
                logging.warning(f"No words found with POS tags: {pos_tags}")
                return []
            logging.info(f"POS extraction found {len(extracted_words)} keywords.")
            return extracted_words
        except Exception as e:
            logging.error(f"An error occurred during POS extraction: {e}")
            return []