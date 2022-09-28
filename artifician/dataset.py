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
import pandas
from rx.subject import Subject


class Dataset:
    """ Dataset contains all the functionality for preparing artifician data
        Dataset has events which are observed by observers (for eg: FeatureDefiniton, Processor)
        All the processed artifician data is stored in datastore
        which is an object of Pandas dataframe

    Attributes:
        cached (dictionary): {event: rx.core.observable.observable.Observable}
        datastore (pandas.core.frame.DataFrame): all the samples are stored in datastore
        PREPARE_DATASET (function): event
        POST_PROCESS (function): event
    """

    def __init__(self):

        self.features_sample = None
        self.cached = {}
        self.datastore = pandas.DataFrame()
        self.PREPARE_DATASET = self.add_samples
        self.POST_PROCESS = self.post_process

    def add_samples(self, samples):
        """
        add samples to the datastore.

        Args:
            samples (any): artifician data

        Return:
            datastore (pandas.core.frame.DataFrame): dataset
        """
        sample_data = []

        if type(samples) is not list: raise TypeError(f"input data should be list not {type(samples)}")

        try:
            for sample in samples:
                self.features_sample = [sample]
                self.cached[self.add_samples].on_next(sample)
                sample_data.append(self.features_sample)
        except KeyError:
            print("No module is listening to dataset")

        self.datastore = pandas.DataFrame(sample_data)

        return self.datastore

    def observe(self, event):
        """ build and return observable for given event. This method is
            called by the observer who wants to listen to the particular event.

        Args:
            event (function): function to create observable from

        Returns:
            observable (rx.core.observable.observable.Observable): Observable
        """

        if event not in self.cached:
            self.cached[event] = Subject()

        return self.cached[event]

    def post_process(self):
        """ This event should be called after artifician data is prepared.
            All the actions that needs to performed collectively on the whole
            dataset should listen to post_process event.
        """

        self.cached[self.post_process].on_next(self.datastore)
