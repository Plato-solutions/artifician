# artifician.dataset module

Copyright 2021 Plato Solutions, Inc.

Licensed under the Apache License, Version 2.0 (the “License”);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

> [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an “AS IS” BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


### _class_ artifician.dataset.Dataset()
Bases: `object`

Dataset contains all the functionality for preparing artifician data

    Dataset has events which are observed by observers (for eg: FeatureDefiniton, Processor)
    All the processed artifician data is stored in datastore
    which is an object of Pandas dataframe

Attributes:

    cached (dictionary): {event: rx.core.observable.observable.Observable}
    datastore (pandas.core.frame.DataFrame): all the samples are stored in datastore
    PREPARE_DATASET (function): event
    POST_PROCESS (function): event


#### add_samples(samples)
add samples to the datastore.

Args:

    samples (any): artifician data

Return:

    datastore (pandas.core.frame.DataFrame): dataset


#### observe(event)
build and return observable for given event. This method is

    called by the observer who wants to listen to the particular event.

Args:

    event (function): function to create observable from

Returns:

    observable (rx.core.observable.observable.Observable): Observable


#### post_process()
This event should be called after artifician data is prepared.
All the actions that needs to performed collectively on the whole
dataset should listen to post_process event.
