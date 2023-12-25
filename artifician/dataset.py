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
import pandas as pd
import logging
from typing import Any, List
from rx.subject import Subject

class Dataset:
    """
    Dataset contains all the functionality for preparing Artifician data.
    It observes events and stores all processed data in a Pandas DataFrame.

    Attributes:
        cached (dict): Cached observables for different events.
        datastore (pd.DataFrame): DataFrame to store all samples.
        PREPARE_DATASET (Callable): Event to prepare the dataset.
        POST_PROCESS (Callable): Event for post-processing actions on the dataset.
    """

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.features_sample = None
        self.cached = {}
        self.datastore = pd.DataFrame()
        self.PREPARE_DATASET = self.add_samples
        self.POST_PROCESS = self.post_process

    def add_samples(self, samples: Any) -> pd.DataFrame:
        """
        Adds samples to the datastore.

        Args:
            samples (Any): Artifician data to be added.

        Returns:
            pd.DataFrame: The updated dataset.

        Raises:
            TypeError: If the input data is not a list.
        """
        if not isinstance(samples, list):
            self.logger.error(f"Input data should be list, not {type(samples)}")
            raise TypeError(f"Input data should be list, not {type(samples)}")

        sample_data = []

        try:
            for sample in samples:
                self.features_sample = [sample]
                if self.add_samples in self.cached:
                    self.cached[self.add_samples].on_next(sample)
                sample_data.append(self.features_sample)
        except KeyError as e:
            self.logger.warning("No module has subscribed to dataset: " + str(e))

        self.datastore = pd.DataFrame(sample_data)
        return self.datastore

    def observe(self, event):
        """
        Builds and returns an observable for a given event.

        Args:
            event (Callable): Function to create an observable from.

        Returns:
            rx.subject.Subject: Observable for the given event.
        """
        if event not in self.cached:
            self.cached[event] = Subject()

        return self.cached[event]

    def post_process(self):
        """
        This event should be called after Artifician data is prepared.
        Listeners to the post_process event can perform collective actions on the dataset.
        """
        if self.post_process in self.cached:
            self.cached[self.post_process].on_next(self.datastore)

