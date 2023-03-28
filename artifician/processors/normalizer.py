"""
   Copyright 2021 Plato Solutions, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from abc import ABC, abstractmethod
import re
from . import processor


class Normalizer(processor.Processor):
    """Normalize the given string value

    Attributes:
        strategy (NormalizerStrategy): strategy for normalizing string
        delimiter (dictionary): delimiter for splitting the string
    """

    def __init__(self, strategy=None, delimiter=None):
        """Initialize the Normalizer by setting up the normalizer strategy and the delimiter

        Args:
            strategy (NormalizerStrategy): NormalizerStrategy instance which normalizes string
            delimiter (dictionary):  delimiter for splitting the string
        """
        self.strategy = strategy
        self.delimiter = delimiter

    def process(self, publisher, feature_raw):
        """Normalize the feature_raw value
        Note : publisher.feature_value is updated instead of returning the value as normalizer
        being a processor

        Args:
            publisher (object): instance of the publisher
            feature_raw (string): feature value

        Returns:
            None
        """
        # if no strategy is provided, an appropriate strategy is selected based on feature_raw value
        if self.strategy is None:
            self.strategy, self.delimiter = StrategySelector().select(feature_raw)

        publisher.value = self.strategy.normalize(feature_raw, self.delimiter)

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


class NormalizerStrategy(ABC):
    """interface for normalizer strategies"""

    @abstractmethod
    def normalize(self, feature_raw, delimiter):
        pass


class PropertiesNormalizer(NormalizerStrategy):
    """Split by delimiter into a format that preserves the sequential position of each value found."""

    def normalize(self, feature_raw, delimiter):
        """split by delimiter into format that preserves sequential position
            of each value in feature text found

        Args:
            delimiter: delimiter is used for breaking string
            feature_raw (string): feature_raw

        Return:
            feature_normalized (list):  list of tuple of normalized feature raw
        """

        feature_raw_values = re.split(f'{delimiter["delimiter"]}', feature_raw)
        feature_normalized = [(value, key) for key, value in enumerate(feature_raw_values)]

        return feature_normalized


class PathsNormalizer(NormalizerStrategy):
    """split by delimiter into a format that preserves position within tree of each value found"""

    @staticmethod
    def get_path_values(feature_raw_values, delimiter):
        """gets path values sequentially

        Args:
            feature_raw_values (list): list of strings
            delimiter (string): delimiter is used for breaking string

        Return:
            feature_normalized (list): list of tuple of normalized feature text values

        """

        path_value, path_values = '', []

        for value in feature_raw_values:
            path_value += value + delimiter[0]
            path_values.append(path_value)

        return path_values

    def normalize(self, feature_raw, delimiter):
        """split by delimiter into a format that preserves position within tree of each value found

        Args:
            feature_raw (string): feature text
            delimiter (dict): delimiter is used for breaking string

        Return:
            feature_normalized (list): list of tuple of normalized feature text values
        """

        feature_raw_values = re.split(f'{delimiter["delimiter"]}', feature_raw)[1:]
        path_values = self.get_path_values(feature_raw_values, delimiter['delimiter'])
        feature_normalized = [(value, key) for key, value in enumerate(path_values)]

        return feature_normalized


class KeyValuesNormalizer(NormalizerStrategy):
    """split by delimiter into a format that preserves value and label association found."""

    @staticmethod
    def normalize_key_values(key_values, assignment):
        """break down text using assignment into key value pair

        Args:
            key_values (list): list of strings
            assignment (string): string that separates key and values

        Return:
            feature_normalized (list): list of tuple of normalized feature text values

        """

        feature_normalized = []

        try:
            for key_value in key_values:
                key, value = key_value.split(assignment)
                feature_normalized.append((value, key))
        except (KeyError, ValueError):
            return []

        return feature_normalized

    def normalize(self, feature_raw, delimiter):
        """split by delimiter into a format that preserves value and label association found.

        Args:
            feature_raw (string): feature_raw
            delimiter: delimiter is used for breaking string

        Return:
            feature_normalized (list): list of tuple of normalized feature text values
        """

        key_values = re.split(f'{delimiter["delimiter"]}', feature_raw)
        feature_normalized = self.normalize_key_values(key_values, delimiter['assignment'])

        return feature_normalized


class StrategySelector:
    """Based on the text input select the appropriate normalizer strategy to normalize the text"""

    def get_paths_delimiter(self, texts):
        """Identify whether the given texts is a paths string if yes return the appropriate delimiter to normalize text

        Args:
            texts (list): list of strings

        Returns:
            Bool (True/False): True if the given texts is identified as paths texts

        """
        delimiter = None
        delimiter_count = 0

        for text in texts:
            delimiter_count += text.count("/")

        if delimiter_count >= len(texts): delimiter = {"delimiter": "/"}

        return delimiter

    def get_key_values_delimiter(self, texts):
        """Identify whether the given texts is a key values string if yes return the appropriate delimiter to normalize text

        Args:
            texts (str): list of strings

        Returns:
            Bool (True/False): True if the given texts is identified as key:values text else returns false

        """
        assignment_operator, delimiter = None, None
        assignment_counts = {"colon_count": 0, "equal_to_count": 0}
        delimiter_counts = {"ampersand_count": 0, "comma_count": 0}

        for text in texts:
            assignment_counts["colon_count"] += text.count(":")
            assignment_counts["equal_to_count"] += text.count("=")
            delimiter_counts["ampersand_count"] += text.count("&")
            delimiter_counts["comma_count"] += text.count(",")

        if assignment_counts["colon_count"] > assignment_counts["equal_to_count"] and assignment_counts["colon_count"] >= len(texts):
            assignment_operator = ":"
        elif assignment_counts["equal_to_count"] >= len(texts):
            assignment_operator = "="
        if assignment_operator:
            if delimiter_counts["ampersand_count"] > delimiter_counts["comma_count"]:
                delimiter = "&"
            elif delimiter_counts["comma_count"] > 0:
                delimiter = ","
            else:
                delimiter = " "
            return {"delimiter": delimiter, "assignment": assignment_operator}

        return None

    def get_properties_delimiter(self, texts):
        """Identify whether the given texts is a properties string if yes return the appropriate delimiter to normalize text

        Args:
            texts (str): list of strings

        Returns:
            delimiter (dict): delimiter to normalize the string
        """

        delimiter_counts = {" ": 0, ",": 0, "-": 0, "_": 0}

        for text in texts:
            delimiter_counts[" "] += text.count(" ")
            delimiter_counts[","] += text.count(",")
            delimiter_counts["-"] += text.count("-")
            delimiter_counts["_"] += text.count("_")

        delimiter = max(zip(delimiter_counts.values(), delimiter_counts.keys()))[1]

        return {"delimiter": delimiter}

    def select(self, texts):
        """

        Args:
            texts(list): list of strings

        Returns:
            strategy_properties (list): list of strategy and properties to normalize the text
        """
        if type(texts) == str: texts = [texts]
        if type(texts) == int or any([isinstance(item, int) for item in texts]): return None

        paths_delimiter, key_values_delimiter, properties_delimiter = self.get_paths_delimiter(texts), self.get_key_values_delimiter(texts), self.get_properties_delimiter(texts)

        if paths_delimiter: return [PathsNormalizer(), paths_delimiter]
        elif key_values_delimiter: return [KeyValuesNormalizer(), key_values_delimiter]
        elif properties_delimiter: return [PropertiesNormalizer(), properties_delimiter]
        else: return []
