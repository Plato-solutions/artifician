# Table of Contents

* [artifician](#artifician)
* [artifician.feature\_definition](#artifician.feature_definition)
  * [FeatureDefinition](#artifician.feature_definition.FeatureDefinition)
    * [\_\_init\_\_](#artifician.feature_definition.FeatureDefinition.__init__)
    * [process](#artifician.feature_definition.FeatureDefinition.process)
    * [map](#artifician.feature_definition.FeatureDefinition.map)
    * [observe](#artifician.feature_definition.FeatureDefinition.observe)
    * [subscribe](#artifician.feature_definition.FeatureDefinition.subscribe)
* [artifician.dataset](#artifician.dataset)
  * [Dataset](#artifician.dataset.Dataset)
    * [add\_samples](#artifician.dataset.Dataset.add_samples)
    * [observe](#artifician.dataset.Dataset.observe)
    * [post\_process](#artifician.dataset.Dataset.post_process)
* [artifician.processors.chain](#artifician.processors.chain)
  * [chain](#artifician.processors.chain.chain)
    * [\_\_init\_\_](#artifician.processors.chain.chain.__init__)
    * [then](#artifician.processors.chain.chain.then)
    * [process](#artifician.processors.chain.chain.process)
    * [subscribe](#artifician.processors.chain.chain.subscribe)
* [artifician.processors.mapper](#artifician.processors.mapper)
  * [Mapper](#artifician.processors.mapper.Mapper)
    * [\_\_init\_\_](#artifician.processors.mapper.Mapper.__init__)
    * [process](#artifician.processors.mapper.Mapper.process)
    * [subscribe](#artifician.processors.mapper.Mapper.subscribe)
  * [FeatureMap](#artifician.processors.mapper.FeatureMap)
    * [get\_value\_id](#artifician.processors.mapper.FeatureMap.get_value_id)
* [artifician.processors](#artifician.processors)
* [artifician.processors.processor](#artifician.processors.processor)
  * [Processor](#artifician.processors.processor.Processor)
    * [process](#artifician.processors.processor.Processor.process)
    * [subscribe](#artifician.processors.processor.Processor.subscribe)
    * [then](#artifician.processors.processor.Processor.then)
* [artifician.processors.text](#artifician.processors.text)
* [artifician.processors.text.text\_cleaner](#artifician.processors.text.text_cleaner)
  * [TextCleaningProcessor](#artifician.processors.text.text_cleaner.TextCleaningProcessor)
    * [\_\_init\_\_](#artifician.processors.text.text_cleaner.TextCleaningProcessor.__init__)
    * [process](#artifician.processors.text.text_cleaner.TextCleaningProcessor.process)
    * [subscribe](#artifician.processors.text.text_cleaner.TextCleaningProcessor.subscribe)
* [artifician.processors.text.stop\_word\_remover](#artifician.processors.text.stop_word_remover)
  * [StopWordsRemoverProcessor](#artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor)
    * [\_\_init\_\_](#artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.__init__)
    * [process](#artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.process)
    * [subscribe](#artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.subscribe)
* [artifician.processors.text.tokenizer](#artifician.processors.text.tokenizer)
  * [TokenizationProcessor](#artifician.processors.text.tokenizer.TokenizationProcessor)
    * [\_\_init\_\_](#artifician.processors.text.tokenizer.TokenizationProcessor.__init__)
    * [process](#artifician.processors.text.tokenizer.TokenizationProcessor.process)
    * [subscribe](#artifician.processors.text.tokenizer.TokenizationProcessor.subscribe)
* [artifician.processors.text.stemlemtizer](#artifician.processors.text.stemlemtizer)
  * [StemLemProcessor](#artifician.processors.text.stemlemtizer.StemLemProcessor)
    * [\_\_init\_\_](#artifician.processors.text.stemlemtizer.StemLemProcessor.__init__)
    * [process](#artifician.processors.text.stemlemtizer.StemLemProcessor.process)
    * [subscribe](#artifician.processors.text.stemlemtizer.StemLemProcessor.subscribe)
* [artifician.processors.normalizer](#artifician.processors.normalizer)
  * [Normalizer](#artifician.processors.normalizer.Normalizer)
    * [\_\_init\_\_](#artifician.processors.normalizer.Normalizer.__init__)
    * [process](#artifician.processors.normalizer.Normalizer.process)
    * [subscribe](#artifician.processors.normalizer.Normalizer.subscribe)
  * [NormalizerStrategy](#artifician.processors.normalizer.NormalizerStrategy)
  * [PropertiesNormalizer](#artifician.processors.normalizer.PropertiesNormalizer)
    * [normalize](#artifician.processors.normalizer.PropertiesNormalizer.normalize)
  * [PathsNormalizer](#artifician.processors.normalizer.PathsNormalizer)
    * [get\_path\_values](#artifician.processors.normalizer.PathsNormalizer.get_path_values)
    * [normalize](#artifician.processors.normalizer.PathsNormalizer.normalize)
  * [KeyValuesNormalizer](#artifician.processors.normalizer.KeyValuesNormalizer)
    * [normalize\_key\_values](#artifician.processors.normalizer.KeyValuesNormalizer.normalize_key_values)
    * [normalize](#artifician.processors.normalizer.KeyValuesNormalizer.normalize)
  * [StrategySelector](#artifician.processors.normalizer.StrategySelector)
    * [get\_paths\_delimiter](#artifician.processors.normalizer.StrategySelector.get_paths_delimiter)
    * [get\_key\_values\_delimiter](#artifician.processors.normalizer.StrategySelector.get_key_values_delimiter)
    * [get\_properties\_delimiter](#artifician.processors.normalizer.StrategySelector.get_properties_delimiter)
    * [select](#artifician.processors.normalizer.StrategySelector.select)
* [artifician.extractors.text\_extractors.keyword\_extractor](#artifician.extractors.text_extractors.keyword_extractor)
  * [KeywordExtractor](#artifician.extractors.text_extractors.keyword_extractor.KeywordExtractor)
    * [\_\_init\_\_](#artifician.extractors.text_extractors.keyword_extractor.KeywordExtractor.__init__)
* [artifician.extractors.html\_extractors](#artifician.extractors.html_extractors)
  * [get\_node\_text](#artifician.extractors.html_extractors.get_node_text)
  * [get\_node\_attribute](#artifician.extractors.html_extractors.get_node_attribute)
  * [get\_parent\_node\_text](#artifician.extractors.html_extractors.get_parent_node_text)
  * [get\_child\_node\_text](#artifician.extractors.html_extractors.get_child_node_text)
  * [count\_child\_nodes](#artifician.extractors.html_extractors.count_child_nodes)
  * [get\_sibling\_node\_text](#artifician.extractors.html_extractors.get_sibling_node_text)
  * [get\_parent\_attribute](#artifician.extractors.html_extractors.get_parent_attribute)
  * [get\_child\_attribute](#artifician.extractors.html_extractors.get_child_attribute)
* [artifician.extractors](#artifician.extractors)

<a id="artifician"></a>

# artifician

<a id="artifician.feature_definition"></a>

# artifician.feature\_definition

<a id="artifician.feature_definition.FeatureDefinition"></a>

## FeatureDefinition Objects

```python
class FeatureDefinition()
```

Contains all the functionality for preparing a single feature.

**Attributes**:

- `value` _Any_ - The value of the feature.
- `cached` _dict_ - Cached observables for different events.
- `extractor` _Callable_ - Function to extract feature value from the artifician.
- `EVENT_PROCESSED` _Callable_ - Event that processes the feature.
- `MAP_VALUES` _Callable_ - Event that maps values of the feature.
- `extractor_parameters` _Tuple_ - Parameters for the extractor function.

<a id="artifician.feature_definition.FeatureDefinition.__init__"></a>

#### \_\_init\_\_

```python
def __init__(extractor: Callable = lambda sample: sample,
             subscribe_to: List = None,
             *extractor_parameters)
```

Initializes a FeatureDefinition instance.

**Arguments**:

- `extractor` _Callable, optional_ - Function to extract feature value.
- `subscribe_to` _List_ - List of publishers to subscribe to.
- `extractor_parameters` - Additional parameters for the extractor.
  

**Raises**:

- `ValueError` - If no publishers are provided to subscribe to.

<a id="artifician.feature_definition.FeatureDefinition.process"></a>

#### process

```python
def process(publisher, sample: Any) -> None
```

Processes the sample to build the feature value.

**Arguments**:

- `sample` _Any_ - The sample data.
- `publisher` - The instance of the publisher.

<a id="artifician.feature_definition.FeatureDefinition.map"></a>

#### map

```python
def map(feature_value: Any) -> None
```

Maps the feature value into an int or list of ints.

**Arguments**:

- `feature_value` _Any_ - The feature value to be mapped.

<a id="artifician.feature_definition.FeatureDefinition.observe"></a>

#### observe

```python
def observe(event: Callable) -> Subject
```

Builds and returns an observable for a given event.

**Arguments**:

- `event` _Callable_ - The function to create an observable from.
  

**Returns**:

- `Observable` - An observable for the given event.

<a id="artifician.feature_definition.FeatureDefinition.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None) -> None
```

Defines logic for subscribing to an event in a publisher.

**Arguments**:

- `publisher` - The publisher instance.
- `pool_scheduler` _optional_ - The scheduler instance for concurrency.

<a id="artifician.dataset"></a>

# artifician.dataset

<a id="artifician.dataset.Dataset"></a>

## Dataset Objects

```python
class Dataset()
```

Dataset contains all the functionality for preparing Artifician data.
It observes events and stores all processed data in a Pandas DataFrame.

**Attributes**:

- `cached` _dict_ - Cached observables for different events.
- `datastore` _pd.DataFrame_ - DataFrame to store all samples.
- `PREPARE_DATASET` _Callable_ - Event to prepare the dataset.
- `POST_PROCESS` _Callable_ - Event for post-processing actions on the dataset.

<a id="artifician.dataset.Dataset.add_samples"></a>

#### add\_samples

```python
def add_samples(samples: Any) -> pd.DataFrame
```

Adds samples to the datastore.

**Arguments**:

- `samples` _Any_ - Artifician data to be added.
  

**Returns**:

- `pd.DataFrame` - The updated dataset.
  

**Raises**:

- `TypeError` - If the input data is not a list.

<a id="artifician.dataset.Dataset.observe"></a>

#### observe

```python
def observe(event)
```

Builds and returns an observable for a given event.

**Arguments**:

- `event` _Callable_ - Function to create an observable from.
  

**Returns**:

- `rx.subject.Subject` - Observable for the given event.

<a id="artifician.dataset.Dataset.post_process"></a>

#### post\_process

```python
def post_process()
```

This event should be called after Artifician data is prepared.
Listeners to the post_process event can perform collective actions on the dataset.

<a id="artifician.processors.chain"></a>

# artifician.processors.chain

<a id="artifician.processors.chain.chain"></a>

## chain Objects

```python
class chain()
```

Manages a chain of processors.

This class handles the sequential execution of a chain of processors and
can subscribe to a publisher to trigger the processing.

**Attributes**:

- `processors` _list_ - A list of processors in the chain.

<a id="artifician.processors.chain.chain.__init__"></a>

#### \_\_init\_\_

```python
def __init__(processors=None) -> None
```

Initializes the chain with an optional list of processors.

**Arguments**:

- `processors` _list, optional_ - An initial list of processors to be managed.

<a id="artifician.processors.chain.chain.then"></a>

#### then

```python
def then(next_processor) -> 'chain'
```

Adds a processor to the end of the chain.

**Arguments**:

- `processor` _Processor_ - The processor to add to the chain.
  

**Returns**:

- `processor_chaining` _chain_ - The chain instance.

<a id="artifician.processors.chain.chain.process"></a>

#### process

```python
def process(publisher, data: any) -> any
```

Processes data sequentially through the chain of processors.

**Arguments**:

- `data` - The data to be processed by the chain.
  

**Returns**:

  The final processed data after passing through all processors.

<a id="artifician.processors.chain.chain.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None) -> None
```

Subscribes the processor chain to a feature definition.

The feature definition will trigger the processing of the chain.

**Arguments**:

- `feature_definition` _publisher_ - The feature definition to subscribe to.

<a id="artifician.processors.mapper"></a>

# artifician.processors.mapper

<a id="artifician.processors.mapper.Mapper"></a>

## Mapper Objects

```python
class Mapper(processor.Processor)
```

Mapper is a processor responsible for mapping/converting feature values to int

**Attributes**:

- `feature_map` _FeatureMap_ - Feature map contains dictionary --> {value: id}
- `map_key_values` _bool_ - True ---> Map both key and value, False ---> map only keys

<a id="artifician.processors.mapper.Mapper.__init__"></a>

#### \_\_init\_\_

```python
def __init__(feature_map, subscribe_to=None, map_key_values=False)
```

initialise Mapper by setting up the feature map

**Arguments**:

- `feature_map` _FeatureMap_ - instance of feature_map
  
- `map_key_values` _Boolean_ - True = map both the key and values, False = map only values

<a id="artifician.processors.mapper.Mapper.process"></a>

#### process

```python
def process(publisher, feature_value)
```

update the feature value of the publisher by mapping features value to int

**Arguments**:

- `publisher` _object_ - instance of the publisher
- `feature_value(string)` - feature_value
  

**Returns**:

  value_id =

<a id="artifician.processors.mapper.Mapper.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Defines logic for subscribing to an event in publisher

**Arguments**:

- `publisher` _object_ - instance of publisher
  
- `pool_scheduler` _rx.scheduler.ThreadPoolScheduler_ - scheduler instance for concurrency
  

**Returns**:

  None

<a id="artifician.processors.mapper.FeatureMap"></a>

## FeatureMap Objects

```python
class FeatureMap()
```

Converts given value to int

**Attributes**:

- `values_map` _dictionary_ - {value : id}

<a id="artifician.processors.mapper.FeatureMap.get_value_id"></a>

#### get\_value\_id

```python
def get_value_id(value)
```

returns the id of the value in values. convert any datatype to str as
dictionary keys can not be of other than str and int. each format can be
converted to str only.

**Arguments**:

- `value` _any_ - value
  

**Returns**:

- `value_id` _int_ - ID of the value

<a id="artifician.processors"></a>

# artifician.processors

<a id="artifician.processors.processor"></a>

# artifician.processors.processor

<a id="artifician.processors.processor.Processor"></a>

## Processor Objects

```python
class Processor(ABC)
```

Interface for processors in the Artifician library, updated for processor chaining.

This abstract class defines the interface for processors, including methods for processing data
and subscribing to publishers, along with the ability to chain processors.

<a id="artifician.processors.processor.Processor.process"></a>

#### process

```python
@abstractmethod
def process(publisher, *data)
```

Process the data and update the publisher with the processed values.

**Arguments**:

- `publisher` - The publisher to which the processed data will be updated.
- `data` - The data to be processed.

<a id="artifician.processors.processor.Processor.subscribe"></a>

#### subscribe

```python
@abstractmethod
def subscribe(publisher, pool_scheduler=None)
```

Subscribe the processor to a publisher (e.g., FeatureDefinition).

**Arguments**:

- `publisher` - The publisher to subscribe to.
- `pool_scheduler` _optional_ - The scheduler to be used for subscription.

<a id="artifician.processors.processor.Processor.then"></a>

#### then

```python
def then(next_processor)
```

Link this processor to the next one in the chain.

**Arguments**:

- `next_processor` - The next processor to add to the chain.
  

**Returns**:

- `chain` - chain of processors
  

**Raises**:

- `TypeError` - If the next_processor is not a valid processor instance.

<a id="artifician.processors.text"></a>

# artifician.processors.text

<a id="artifician.processors.text.text_cleaner"></a>

# artifician.processors.text.text\_cleaner

<a id="artifician.processors.text.text_cleaner.TextCleaningProcessor"></a>

## TextCleaningProcessor Objects

```python
class TextCleaningProcessor(Processor)
```

Processor for cleaning and preprocessing text data.

Configurable attributes for various cleaning operations.

<a id="artifician.processors.text.text_cleaner.TextCleaningProcessor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(lowercase=True,
             remove_punctuation=True,
             remove_numbers=True,
             strip_whitespace=True,
             remove_html_tags=True,
             remove_urls=True,
             subscribe_to=None)
```

Initialize a TextCleaningProcessor object.

**Arguments**:

- `lowercase` _bool_ - Flag to convert text to lowercase.
- `remove_punctuation` _bool_ - Flag to remove punctuation.
- `remove_numbers` _bool_ - Flag to remove numbers.
- `strip_whitespace` _bool_ - Flag to strip extra whitespaces.
- `remove_html_tags` _bool_ - Flag to remove HTML tags.
- `remove_urls` _bool_ - Flag to remove URLs.
- `custom_stop_words` _List[str]_ - Optional list of custom stop words.
- `subscribe_to` _list_ - Optional list of publishers to subscribe to.

<a id="artifician.processors.text.text_cleaner.TextCleaningProcessor.process"></a>

#### process

```python
def process(publisher, text: Union[str, List[str]]) -> Union[str, List[str]]
```

Process the text or list of texts to clean and preprocess.

**Arguments**:

- `publisher` - The publisher associated with the processor.
- `text` _Union[str, List[str]]_ - The text or list of texts to be processed.
  

**Returns**:

  Union[str, List[str]]: Cleaned and preprocessed text.

<a id="artifician.processors.text.text_cleaner.TextCleaningProcessor.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Subscribe to a publisher for event-driven processing.

**Arguments**:

- `publisher` _object_ - The publisher to subscribe to.
- `pool_scheduler` _optional_ - Scheduler instance for concurrency.
  

**Returns**:

  None

<a id="artifician.processors.text.stop_word_remover"></a>

# artifician.processors.text.stop\_word\_remover

<a id="artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor"></a>

## StopWordsRemoverProcessor Objects

```python
class StopWordsRemoverProcessor(Processor)
```

Processor for removing stop words from text data.

**Attributes**:

- `stop_words` _set_ - A set of stop words to be removed.

<a id="artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(custom_stop_words: List[str] = None, subscribe_to=None)
```

Initialize a StopWordsRemoverProcessor object.

**Arguments**:

- `custom_stop_words` _List[str]_ - Optional list of custom stop words.
- `subscribe_to` _list_ - Optional list of publishers to subscribe to.

<a id="artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.process"></a>

#### process

```python
def process(publisher, text: Union[str, List[str]]) -> Union[str, List[str]]
```

Process the text or list of texts to remove stop words.

**Arguments**:

- `publisher` - The publisher associated with the processor.
- `text` _Union[str, List[str]]_ - The text or list of texts to be processed.
  

**Returns**:

  Union[str, List[str]]: Text after stop words removal.
  

**Raises**:

- `ValueError` - If the input text is None or an empty list.

<a id="artifician.processors.text.stop_word_remover.StopWordsRemoverProcessor.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Subscribe to a publisher for event-driven processing.

**Arguments**:

- `publisher` _object_ - The publisher to subscribe to.
- `pool_scheduler` _optional_ - Scheduler instance for concurrency.
  

**Returns**:

  None

<a id="artifician.processors.text.tokenizer"></a>

# artifician.processors.text.tokenizer

<a id="artifician.processors.text.tokenizer.TokenizationProcessor"></a>

## TokenizationProcessor Objects

```python
class TokenizationProcessor(Processor)
```

Tokenization Processor for splitting text into tokens.

**Attributes**:

- `method` _str_ - Method to use for tokenization ('word' or 'sentence').
- `nlp` - spaCy language model for processing text.

<a id="artifician.processors.text.tokenizer.TokenizationProcessor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(method: str = 'word', subscribe_to=None)
```

Initialize a TokenizationProcessor object.

**Arguments**:

- `method` _str_ - Method to use for tokenization ('word' or 'sentence').

<a id="artifician.processors.text.tokenizer.TokenizationProcessor.process"></a>

#### process

```python
def process(
        publisher, text: Union[str, List[str],
                               None]) -> Union[List[str], List[List[str]]]
```

Process the text or list of texts and split it into tokens.

**Arguments**:

- `text` _Union[str, List[str], None]_ - The text or list of texts to be tokenized.
  

**Returns**:

  Union[List[str], List[List[str]]]: A list of tokens or list of lists of tokens.
  

**Raises**:

- `ValueError` - If the input text is None or an empty list.

<a id="artifician.processors.text.tokenizer.TokenizationProcessor.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Defines logic for subscribing to an event in publisher

**Arguments**:

- `publisher` _object_ - instance of the publisher
- `pool_scheduler` _rx.scheduler.ThreadPoolScheduler_ - scheduler instance for concurrency
  

**Returns**:

  None

<a id="artifician.processors.text.stemlemtizer"></a>

# artifician.processors.text.stemlemtizer

<a id="artifician.processors.text.stemlemtizer.StemLemProcessor"></a>

## StemLemProcessor Objects

```python
class StemLemProcessor(Processor)
```

Processor for applying stemming and lemmatization to text data.

**Attributes**:

- `mode` _str_ - Mode of operation ('stemming' or 'lemmatization').
- `nlp` - spaCy language model for lemmatization.
- `stemmer` - NLTK stemmer for stemming.

<a id="artifician.processors.text.stemlemtizer.StemLemProcessor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mode: str = 'lemmatization', subscribe_to=None)
```

Initialize a StemLemProcessor object.

**Arguments**:

- `mode` _str_ - Operation mode ('stemming' or 'lemmatization').
- `subscribe_to` _list_ - Optional list of publishers to subscribe to.

<a id="artifician.processors.text.stemlemtizer.StemLemProcessor.process"></a>

#### process

```python
def process(publisher, text: Union[str, List[str]]) -> Union[str, List[str]]
```

Process the text or list of tokens for stemming or lemmatization.

**Arguments**:

- `publisher` - The publisher associated with the processor.
- `text` _Union[str, List[str]]_ - The text or list of tokens to be processed.
  

**Returns**:

  Union[str, List[str]]: Processed text or list of processed tokens.

<a id="artifician.processors.text.stemlemtizer.StemLemProcessor.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Subscribe to a publisher for event-driven processing.

**Arguments**:

- `publisher` _object_ - The publisher to subscribe to.
- `pool_scheduler` _optional_ - Scheduler instance for concurrency.
  

**Returns**:

  None

<a id="artifician.processors.normalizer"></a>

# artifician.processors.normalizer

<a id="artifician.processors.normalizer.Normalizer"></a>

## Normalizer Objects

```python
class Normalizer(processor.Processor)
```

Normalize the given string value

**Attributes**:

- `strategy` _NormalizerStrategy_ - strategy for normalizing string
- `delimiter` _dictionary_ - delimiter for splitting the string

<a id="artifician.processors.normalizer.Normalizer.__init__"></a>

#### \_\_init\_\_

```python
def __init__(strategy=None, subscribe_to=None, delimiter=None)
```

Initialize the Normalizer by setting up the normalizer strategy and the delimiter

**Arguments**:

- `strategy` _NormalizerStrategy_ - NormalizerStrategy instance which normalizes string
- `delimiter` _dictionary_ - delimiter for splitting the string

<a id="artifician.processors.normalizer.Normalizer.process"></a>

#### process

```python
def process(publisher, feature_raw)
```

Normalize the feature_raw value
Note : publisher.feature_value is updated instead of returning the value as normalizer
being a processor

**Arguments**:

- `publisher` _object_ - instance of the publisher
- `feature_raw` _string_ - feature value
  

**Returns**:

  None

<a id="artifician.processors.normalizer.Normalizer.subscribe"></a>

#### subscribe

```python
def subscribe(publisher, pool_scheduler=None)
```

Defines logic for subscribing to an event in publisher

**Arguments**:

- `publisher` _object_ - instance of the publisher
- `pool_scheduler` _rx.scheduler.ThreadPoolScheduler_ - scheduler instance for concurrency
  

**Returns**:

  None

<a id="artifician.processors.normalizer.NormalizerStrategy"></a>

## NormalizerStrategy Objects

```python
class NormalizerStrategy(ABC)
```

interface for normalizer strategies

<a id="artifician.processors.normalizer.PropertiesNormalizer"></a>

## PropertiesNormalizer Objects

```python
class PropertiesNormalizer(NormalizerStrategy)
```

Split by delimiter into a format that preserves the sequential position of each value found.

<a id="artifician.processors.normalizer.PropertiesNormalizer.normalize"></a>

#### normalize

```python
def normalize(feature_raw, delimiter)
```

split by delimiter into format that preserves sequential position
of each value in feature text found

**Arguments**:

- `delimiter` - delimiter is used for breaking string
- `feature_raw` _string_ - feature_raw
  

**Returns**:

- `feature_normalized` _list_ - list of tuple of normalized feature raw

<a id="artifician.processors.normalizer.PathsNormalizer"></a>

## PathsNormalizer Objects

```python
class PathsNormalizer(NormalizerStrategy)
```

split by delimiter into a format that preserves position within tree of each value found

<a id="artifician.processors.normalizer.PathsNormalizer.get_path_values"></a>

#### get\_path\_values

```python
@staticmethod
def get_path_values(feature_raw_values, delimiter)
```

gets path values sequentially

**Arguments**:

- `feature_raw_values` _list_ - list of strings
- `delimiter` _string_ - delimiter is used for breaking string
  

**Returns**:

- `feature_normalized` _list_ - list of tuple of normalized feature text values

<a id="artifician.processors.normalizer.PathsNormalizer.normalize"></a>

#### normalize

```python
def normalize(feature_raw, delimiter)
```

split by delimiter into a format that preserves position within tree of each value found

**Arguments**:

- `feature_raw` _string_ - feature text
- `delimiter` _dict_ - delimiter is used for breaking string
  

**Returns**:

- `feature_normalized` _list_ - list of tuple of normalized feature text values

<a id="artifician.processors.normalizer.KeyValuesNormalizer"></a>

## KeyValuesNormalizer Objects

```python
class KeyValuesNormalizer(NormalizerStrategy)
```

split by delimiter into a format that preserves value and label association found.

<a id="artifician.processors.normalizer.KeyValuesNormalizer.normalize_key_values"></a>

#### normalize\_key\_values

```python
@staticmethod
def normalize_key_values(key_values, assignment)
```

break down text using assignment into key value pair

**Arguments**:

- `key_values` _list_ - list of strings
- `assignment` _string_ - string that separates key and values
  

**Returns**:

- `feature_normalized` _list_ - list of tuple of normalized feature text values

<a id="artifician.processors.normalizer.KeyValuesNormalizer.normalize"></a>

#### normalize

```python
def normalize(feature_raw, delimiter)
```

split by delimiter into a format that preserves value and label association found.

**Arguments**:

- `feature_raw` _string_ - feature_raw
- `delimiter` - delimiter is used for breaking string
  

**Returns**:

- `feature_normalized` _list_ - list of tuple of normalized feature text values

<a id="artifician.processors.normalizer.StrategySelector"></a>

## StrategySelector Objects

```python
class StrategySelector()
```

Based on the text input select the appropriate normalizer strategy to normalize the text

<a id="artifician.processors.normalizer.StrategySelector.get_paths_delimiter"></a>

#### get\_paths\_delimiter

```python
def get_paths_delimiter(texts)
```

Identify whether the given texts is a paths string if yes return the appropriate delimiter to normalize text

**Arguments**:

- `texts` _list_ - list of strings
  

**Returns**:

- `Bool` _True/False_ - True if the given texts is identified as paths texts

<a id="artifician.processors.normalizer.StrategySelector.get_key_values_delimiter"></a>

#### get\_key\_values\_delimiter

```python
def get_key_values_delimiter(texts)
```

Identify whether the given texts is a key values string if yes return the appropriate delimiter to normalize text

**Arguments**:

- `texts` _str_ - list of strings
  

**Returns**:

- `Bool` _True/False_ - True if the given texts is identified as key:values text else returns false

<a id="artifician.processors.normalizer.StrategySelector.get_properties_delimiter"></a>

#### get\_properties\_delimiter

```python
def get_properties_delimiter(texts)
```

Identify whether the given texts is a properties string if yes return the appropriate delimiter to normalize text

**Arguments**:

- `texts` _str_ - list of strings
  

**Returns**:

- `delimiter` _dict_ - delimiter to normalize the string

<a id="artifician.processors.normalizer.StrategySelector.select"></a>

#### select

```python
def select(texts)
```

**Arguments**:

- `texts(list)` - list of strings
  

**Returns**:

- `strategy_properties` _list_ - list of strategy and properties to normalize the text

<a id="artifician.extractors.text_extractors.keyword_extractor"></a>

# artifician.extractors.text\_extractors.keyword\_extractor

<a id="artifician.extractors.text_extractors.keyword_extractor.KeywordExtractor"></a>

## KeywordExtractor Objects

```python
class KeywordExtractor()
```

Keyword Extractor class for extracting specific keywords from a text.

**Attributes**:

- `method` _str_ - Method to use for keyword extraction ('manual', 'frequency', 'tfidf', etc.)
- `keywords` _List[str]_ - List of keywords to search within the text for 'manual' method.

<a id="artifician.extractors.text_extractors.keyword_extractor.KeywordExtractor.__init__"></a>

#### \_\_init\_\_

```python
def __init__(method: str = 'manual', keywords: List[str] = None)
```

Initialize a new KeywordExtractor object.

**Arguments**:

- `method` _str_ - Method to use for keyword extraction.
- `keywords` _List[str]_ - List of keywords to search within the text for 'manual' method.
  

**Raises**:

- `ValueError` - If the keywords list is empty for 'manual' method.

<a id="artifician.extractors.html_extractors"></a>

# artifician.extractors.html\_extractors

<a id="artifician.extractors.html_extractors.get_node_text"></a>

#### get\_node\_text

```python
def get_node_text(node: List[Union[str, Tag]]) -> str
```

Extracts text from a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to extract text from.
  

**Returns**:

- `str` - The text content of the node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.
- `ValueError` - If the node list is empty.

<a id="artifician.extractors.html_extractors.get_node_attribute"></a>

#### get\_node\_attribute

```python
def get_node_attribute(node: List[Union[str, Tag]], attribute: str) -> str
```

Retrieves the value of a specified attribute from a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to get the attribute from.
- `attribute` _str_ - The name of the attribute to retrieve.
  

**Returns**:

- `str` - The value of the attribute.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.get_parent_node_text"></a>

#### get\_parent\_node\_text

```python
def get_parent_node_text(node: List[Union[str, Tag]]) -> str
```

Extracts text from the parent node of a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to extract parent text from.
  

**Returns**:

- `str` - The text content of the parent node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.get_child_node_text"></a>

#### get\_child\_node\_text

```python
def get_child_node_text(node: List[Union[str, Tag]]) -> str
```

Extracts text from the first child node of a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to extract child text from.
  

**Returns**:

- `str` - The text content of the child node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.count_child_nodes"></a>

#### count\_child\_nodes

```python
def count_child_nodes(node: List[Union[str, Tag]]) -> int
```

Counts the number of child nodes for a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to count children for.
  

**Returns**:

- `int` - The number of child nodes.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.get_sibling_node_text"></a>

#### get\_sibling\_node\_text

```python
def get_sibling_node_text(node: List[Union[str, Tag]]) -> str
```

Extracts text from the first sibling node of a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to extract sibling text from.
  

**Returns**:

- `str` - The text content of the sibling node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.get_parent_attribute"></a>

#### get\_parent\_attribute

```python
def get_parent_attribute(node: List[Union[str, Tag]], attribute: str) -> str
```

Retrieves the value of a specified attribute from the parent of a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to get the parent attribute from.
- `attribute` _str_ - The name of the attribute to retrieve.
  

**Returns**:

- `str` - The value of the attribute from the parent node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors.html_extractors.get_child_attribute"></a>

#### get\_child\_attribute

```python
def get_child_attribute(node: List[Union[str, Tag]], attribute: str) -> str
```

Retrieves the value of a specified attribute from the first child of a given node.

**Arguments**:

- `node` _List[Union[str, Tag]]_ - The node list to get the child attribute from.
- `attribute` _str_ - The name of the attribute to retrieve.
  

**Returns**:

- `str` - The value of the attribute from the child node.
  

**Raises**:

- `TypeError` - If the first element in the node list is not a bs4.element.Tag.

<a id="artifician.extractors"></a>

# artifician.extractors

