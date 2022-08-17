# artifician.processors.normalizer module


### _class_ artifician.processors.normalizer.KeyValuesNormalizer()
Bases: `artifician.processors.normalizer.NormalizerStrategy`

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
Bases: [`artifician.processors.processor.Processor`](artifician.processors.processor.md#artifician.processors.processor.Processor)

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
Bases: `abc.ABC`

interface for normalizer strategies


#### _abstract_ normalize(feature_raw, delimiter)

### _class_ artifician.processors.normalizer.PathsNormalizer()
Bases: `artifician.processors.normalizer.NormalizerStrategy`

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
Bases: `artifician.processors.normalizer.NormalizerStrategy`

Split by delimiter into a format that preserves the sequential position of each value found.


#### normalize(feature_raw, delimiter)
split by delimiter into format that preserves sequential position

    of each value in feature text found

Args:

    delimiter: delimiter is used for breaking string
    feature_raw (string): feature_raw

Return:

    feature_normalized (list):  list of tuple of normalized feature raw
