# artifician.processors.processor module

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


### _class_ artifician.processors.processor.Processor()
Bases: `ABC`

interface for the processors


#### _abstract_ process(publisher, \*data)
Defines the logic for processing data
Do not return the processed values, update the appropriate attribute of publisher instead.

For e.g. if processor is subscribed to FeatureDefinition(publisher)
then update feature_value attribute  of the feature definition
publisher.feature_value = <processed_value>
see other predefined processor for clear understanding


#### _abstract_ subscribe(publisher, pool_scheduler=None)
Defines logic for subscribing to an event in publisher
