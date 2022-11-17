# artifician.processors.normalizer module

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


### _class_ artifician.processors.normalizer.KeyValuesNormalizer()
Bases: `NormalizerStrategy`

split by delimiter into a format that preserves value and label association found.


#### normalize(feature_raw, delimiter)
split by delimiter into a format that preserves value and label association found.

Args:

    feature_raw (string): feature_raw
    delimiter: delimiter is used for breaking string

Return:

    feature_normalized (list): list of tuple of normalized feature text values


#### _static_ normalize_key_values(key_values, assignment)
break down text using assignment into key value pair

Args:

    key_values (list): list of strings
    assignment (string): string that separates key and values

Return:

    feature_normalized (list): list of tuple of normalized feature text values


### _class_ artifician.processors.normalizer.Normalizer(strategy, delimiter)
Bases: [`Processor`](artifician.processors.processor.md#artifician.processors.processor.Processor)

Normalize the given string value

Attributes:

    strategy (NormalizerStrategy): strategy for normalizing string
    delimiter (dictionary): delimiter for splitting the string


#### process(publisher, feature_raw)
Normalize the feature_raw value
Note : publisher.feature_value is updated instead of returning the value as normalizer
being a processor

Args:

    publisher (object): instance of the publisher
    feature_raw (string): feature value

Returns:

    None


#### subscribe(publisher, pool_scheduler=None)
Defines logic for subscribing to an event in publisher

Args:

    publisher (object): instance of the publisher
    pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Returns:

    None


### _class_ artifician.processors.normalizer.NormalizerStrategy()
Bases: `ABC`

interface for normalizer strategies


#### _abstract_ normalize(feature_raw, delimiter)

### _class_ artifician.processors.normalizer.PathsNormalizer()
Bases: `NormalizerStrategy`

split by delimiter into a format that preserves position within tree of each value found


#### _static_ get_path_values(feature_raw_values, delimiter)
gets path values sequentially

Args:

    feature_raw_values (list): list of strings
    delimiter (string): delimiter is used for breaking string

Return:

    feature_normalized (list): list of tuple of normalized feature text values


#### normalize(feature_raw, delimiter)
split by delimiter into a format that preserves position within tree of each value found

Args:

    feature_raw (string): feature text
    delimiter (dict): delimiter is used for breaking string

Return:

    feature_normalized (list): list of tuple of normalized feature text values


### _class_ artifician.processors.normalizer.PropertiesNormalizer()
Bases: `NormalizerStrategy`

Split by delimiter into a format that preserves the sequential position of each value found.


#### normalize(feature_raw, delimiter)
split by delimiter into format that preserves sequential position

    of each value in feature text found

Args:

    delimiter: delimiter is used for breaking string
    feature_raw (string): feature_raw

Return:

    feature_normalized (list):  list of tuple of normalized feature raw
