"""
   Copyright 2023 Plato Solutions, Inc.

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
import logging
from typing import Tuple, Any, Callable, List
from rx.subject import Subject

class FeatureDefinition:
    """
    Contains all the functionality for preparing a single feature.

    Attributes:
        value (Any): The value of the feature.
        cached (dict): Cached observables for different events.
        extractor (Callable): Function to extract feature value from the artifician.
        EVENT_PROCESSED (Callable): Event that processes the feature.
        MAP_VALUES (Callable): Event that maps values of the feature.
        extractor_parameters (Tuple): Parameters for the extractor function.
    """

    def __init__(self, extractor: Callable = lambda sample: sample, subscribe_to: List = None, *extractor_parameters):
        """
        Initializes a FeatureDefinition instance.

        Args:
            extractor (Callable, optional): Function to extract feature value.
            subscribe_to (List): List of publishers to subscribe to.
            extractor_parameters: Additional parameters for the extractor.

        Raises:
            ValueError: If no publishers are provided to subscribe to.
        """
        self.logger = logging.getLogger(__name__)

        if not subscribe_to:
            self.logger.error("FeatureDefinition must be subscribed to at least one publisher.")
            raise ValueError("FeatureDefinition must be subscribed to at least one publisher.")

        self.value = None
        self.cached = {}
        self.extractor = extractor
        self.extractor_parameters = extractor_parameters
        self.EVENT_PROCESSED = self.process
        self.MAP_VALUES = self.map

        for publisher in subscribe_to:
            self.subscribe(publisher)

    def process(self, publisher, sample: Any) -> None:
        """
        Processes the sample to build the feature value.

        Args:
            sample (Any): The sample data.
            publisher: The instance of the publisher.
        """
        try:
            self.value = self.extractor(sample, *self.extractor_parameters)

            if self.process in self.cached:
                self.cached[self.process].on_next(self.value)

            self.map(self.value)
            publisher.features_sample.append(self.value)
        except Exception as e:
            self.logger.exception(f"Error in processing feature: {e}")
            raise

    def map(self, feature_value: Any) -> None:
        """
        Maps the feature value into an int or list of ints.

        Args:
            feature_value (Any): The feature value to be mapped.
        """
        try:
            if self.map in self.cached:
                self.cached[self.map].on_next(feature_value)
        except Exception as e:
            self.logger.exception(f"Error in mapping feature value: {e}")
            raise

    def observe(self, event: Callable) -> Subject:
        """
        Builds and returns an observable for a given event.

        Args:
            event (Callable): The function to create an observable from.

        Returns:
            Observable: An observable for the given event.
        """
        if event not in self.cached:
            self.cached[event] = Subject()

        return self.cached[event]

    def subscribe(self, publisher, pool_scheduler=None) -> None:
        """
        Defines logic for subscribing to an event in a publisher.

        Args:
            publisher: The publisher instance.
            pool_scheduler (optional): The scheduler instance for concurrency.
        """
        try:
            observable = publisher.observe(publisher.PREPARE_DATASET)
            observable.subscribe(lambda feature_raw: self.process(publisher, feature_raw),
                                 scheduler=pool_scheduler)
        except AttributeError as e:
            self.logger.error(f"Failed to subscribe to publisher: {e}")
            raise
