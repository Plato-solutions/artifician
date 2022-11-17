# artifician.processors.mapper module

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


### _class_ artifician.processors.mapper.FeatureMap(values_map={})
Bases: `object`

Converts given value to int

Attributes:

    values_map (dictionary): {value : id}


#### get_value_id(value)
returns the id of the value in values. convert any datatype to str as
dictionary keys can not be of other than str and int. each format can be
converted to str only.

Args:

    value (any): value

Return:

    value_id (int):  ID of the value


### _class_ artifician.processors.mapper.Mapper(feature_map, map_key_values=False)
Bases: [`Processor`](artifician.processors.processor.md#artifician.processors.processor.Processor)

Mapper is a processor responsible for mapping/converting feature values to int

Attributes:

    feature_map (FeatureMap): Feature map contains dictionary –> {value: id}
    map_key_values (bool): True —> Map both key and value, False —> map only keys


#### process(publisher, feature_value)
update the feature value of the publisher by mapping features value to int

Args:

    publisher (object): instance of the publisher
    feature_value(string): feature_value

Returns:

    value_id =


#### subscribe(publisher, pool_scheduler=None)
Defines logic for subscribing to an event in publisher

Args:

    publisher (object): instance of publisher

    pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Return:

    None
