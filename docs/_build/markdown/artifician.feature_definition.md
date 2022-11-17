# artifician.feature_definition module

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


### _class_ artifician.feature_definition.FeatureDefinition(extractor=<function FeatureDefinition.<lambda>>, \*extractor_parameters)
Bases: `object`

Contains all the functionality for preparing single feature

Attributes:

    value (any): value of the feature
    cached (dictionary): {event: rx.core.observable.observable.Observable}
    extractor (function): extract feature value from the artifician
    EVENT_PROCESSED (function): event that processes the feature
    MAP_VALUES (function): event that maps values of feature
    extractor_parameters (

    ```
    *
    ```

    args): parameters for extractor function


#### map(feature_value)
Map the feature value from into int or list of int

Args:

    feature_value (any): feature value that needs to be mapped

Return:

    None


#### observe(event)
build and return observable for given event

Args:

    event (function): function to create observable from

Return:

    observable (rx.core.observable.observable.Observable): Observable


#### process(publisher, sample)
process the sample to build feature value
process should contain all the logic for completely processing the feature value

Args:

    sample (any): sample data
    publisher (object): instance of publisher

Return:

    feature_processed (list): processed feature_raw


#### subscribe(publisher, pool_scheduler=None)
Defines logic for subscribing to an event in publisher

Args:

    publisher (object): publisher instance
    pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Return:

    None
