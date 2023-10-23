# artifician.processors package

## artifician.processors.mapper module

### *class* artifician.processors.mapper.FeatureMap(values_map={})

Bases: `object`

Converts given value to int

Attributes:
: values_map (dictionary): {value : id}

#### get_value_id(value)

returns the id of the value in values. convert any datatype to str as
dictionary keys can not be of other than str and int. each format can be
converted to str only.

Args:
: value (any): value

Return:
: value_id (int):  ID of the value

### *class* artifician.processors.mapper.Mapper(feature_map, map_key_values=False)

Bases: [`Processor`](#artifician.processors.processor.Processor)

Mapper is a processor responsible for mapping/converting feature values to int

Attributes:
: feature_map (FeatureMap): Feature map contains dictionary –> {value: id}
  map_key_values (bool): True —> Map both key and value, False —> map only keys

#### process(publisher, feature_value)

update the feature value of the publisher by mapping features value to int

Args:
: publisher (object): instance of the publisher
  feature_value(string): feature_value

Returns:
: value_id =

#### subscribe(publisher, pool_scheduler=None)

Defines logic for subscribing to an event in publisher

Args:
: publisher (object): instance of publisher
  <br/>
  pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Return:
: None

## artifician.processors.normalizer module

### *class* artifician.processors.normalizer.KeyValuesNormalizer

Bases: [`NormalizerStrategy`](#artifician.processors.normalizer.NormalizerStrategy)

split by delimiter into a format that preserves value and label association found.

#### normalize(feature_raw, delimiter)

split by delimiter into a format that preserves value and label association found.

Args:
: feature_raw (string): feature_raw
  delimiter: delimiter is used for breaking string

Return:
: feature_normalized (list): list of tuple of normalized feature text values

#### *static* normalize_key_values(key_values, assignment)

break down text using assignment into key value pair

Args:
: key_values (list): list of strings
  assignment (string): string that separates key and values

Return:
: feature_normalized (list): list of tuple of normalized feature text values

### *class* artifician.processors.normalizer.Normalizer(strategy=None, delimiter=None)

Bases: [`Processor`](#artifician.processors.processor.Processor)

Normalize the given string value

Attributes:
: strategy (NormalizerStrategy): strategy for normalizing string
  delimiter (dictionary): delimiter for splitting the string

#### process(publisher, feature_raw)

Normalize the feature_raw value
Note : publisher.feature_value is updated instead of returning the value as normalizer
being a processor

Args:
: publisher (object): instance of the publisher
  feature_raw (string): feature value

Returns:
: None

#### subscribe(publisher, pool_scheduler=None)

Defines logic for subscribing to an event in publisher

Args:
: publisher (object): instance of the publisher
  pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Returns:
: None

### *class* artifician.processors.normalizer.NormalizerStrategy

Bases: `ABC`

interface for normalizer strategies

#### *abstract* normalize(feature_raw, delimiter)

### *class* artifician.processors.normalizer.PathsNormalizer

Bases: [`NormalizerStrategy`](#artifician.processors.normalizer.NormalizerStrategy)

split by delimiter into a format that preserves position within tree of each value found

#### *static* get_path_values(feature_raw_values, delimiter)

gets path values sequentially

Args:
: feature_raw_values (list): list of strings
  delimiter (string): delimiter is used for breaking string

Return:
: feature_normalized (list): list of tuple of normalized feature text values

#### normalize(feature_raw, delimiter)

split by delimiter into a format that preserves position within tree of each value found

Args:
: feature_raw (string): feature text
  delimiter (dict): delimiter is used for breaking string

Return:
: feature_normalized (list): list of tuple of normalized feature text values

### *class* artifician.processors.normalizer.PropertiesNormalizer

Bases: [`NormalizerStrategy`](#artifician.processors.normalizer.NormalizerStrategy)

Split by delimiter into a format that preserves the sequential position of each value found.

#### normalize(feature_raw, delimiter)

split by delimiter into format that preserves sequential position
: of each value in feature text found

Args:
: delimiter: delimiter is used for breaking string
  feature_raw (string): feature_raw

Return:
: feature_normalized (list):  list of tuple of normalized feature raw

### *class* artifician.processors.normalizer.StrategySelector

Bases: `object`

Based on the text input select the appropriate normalizer strategy to normalize the text

#### get_key_values_delimiter(texts)

Identify whether the given texts is a key values string if yes return the appropriate delimiter to normalize text

Args:
: texts (str): list of strings

Returns:
: Bool (True/False): True if the given texts is identified as key:values text else returns false

#### get_paths_delimiter(texts)

Identify whether the given texts is a paths string if yes return the appropriate delimiter to normalize text

Args:
: texts (list): list of strings

Returns:
: Bool (True/False): True if the given texts is identified as paths texts

#### get_properties_delimiter(texts)

Identify whether the given texts is a properties string if yes return the appropriate delimiter to normalize text

Args:
: texts (str): list of strings

Returns:
: delimiter (dict): delimiter to normalize the string

#### select(texts)

Args:
: texts(list): list of strings

Returns:
: strategy_properties (list): list of strategy and properties to normalize the text

## artifician.processors.processor module

### *class* artifician.processors.processor.Processor

Bases: `ABC`

interface for the processors

#### *abstract* process(publisher, \*data)

Defines the logic for processing data
Do not return the processed values, update the appropriate attribute of publisher instead.

For e.g. if processor is subscribed to FeatureDefinition(publisher)
then update feature_value attribute  of the feature definition
publisher.feature_value = <processed_value>
see other predefined processor for clear understanding

#### *abstract* subscribe(publisher, pool_scheduler=None)

Defines logic for subscribing to an event in publisher

## Module contents
