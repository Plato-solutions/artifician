# artifician package

## Subpackages

* [artifician.extractors package](artifician.extractors.md)
  * [artifician.extractors.html_extractors module](artifician.extractors.md#module-artifician.extractors.html_extractors)
    * [`count_child_nodes()`](artifician.extractors.md#artifician.extractors.html_extractors.count_child_nodes)
    * [`get_child_attribute()`](artifician.extractors.md#artifician.extractors.html_extractors.get_child_attribute)
    * [`get_child_node_text()`](artifician.extractors.md#artifician.extractors.html_extractors.get_child_node_text)
    * [`get_node_attribute()`](artifician.extractors.md#artifician.extractors.html_extractors.get_node_attribute)
    * [`get_node_text()`](artifician.extractors.md#artifician.extractors.html_extractors.get_node_text)
    * [`get_parent_attribute()`](artifician.extractors.md#artifician.extractors.html_extractors.get_parent_attribute)
    * [`get_parent_node_text()`](artifician.extractors.md#artifician.extractors.html_extractors.get_parent_node_text)
    * [`get_sibling_node_text()`](artifician.extractors.md#artifician.extractors.html_extractors.get_sibling_node_text)
  * [Module contents](artifician.extractors.md#module-artifician.extractors)
* [artifician.processors package](artifician.processors.md)
  * [artifician.processors.mapper module](artifician.processors.md#module-artifician.processors.mapper)
    * [`FeatureMap`](artifician.processors.md#artifician.processors.mapper.FeatureMap)
      * [`FeatureMap.get_value_id()`](artifician.processors.md#artifician.processors.mapper.FeatureMap.get_value_id)
    * [`Mapper`](artifician.processors.md#artifician.processors.mapper.Mapper)
      * [`Mapper.process()`](artifician.processors.md#artifician.processors.mapper.Mapper.process)
      * [`Mapper.subscribe()`](artifician.processors.md#artifician.processors.mapper.Mapper.subscribe)
  * [artifician.processors.normalizer module](artifician.processors.md#module-artifician.processors.normalizer)
    * [`KeyValuesNormalizer`](artifician.processors.md#artifician.processors.normalizer.KeyValuesNormalizer)
      * [`KeyValuesNormalizer.normalize()`](artifician.processors.md#artifician.processors.normalizer.KeyValuesNormalizer.normalize)
      * [`KeyValuesNormalizer.normalize_key_values()`](artifician.processors.md#artifician.processors.normalizer.KeyValuesNormalizer.normalize_key_values)
    * [`Normalizer`](artifician.processors.md#artifician.processors.normalizer.Normalizer)
      * [`Normalizer.process()`](artifician.processors.md#artifician.processors.normalizer.Normalizer.process)
      * [`Normalizer.subscribe()`](artifician.processors.md#artifician.processors.normalizer.Normalizer.subscribe)
    * [`NormalizerStrategy`](artifician.processors.md#artifician.processors.normalizer.NormalizerStrategy)
      * [`NormalizerStrategy.normalize()`](artifician.processors.md#artifician.processors.normalizer.NormalizerStrategy.normalize)
    * [`PathsNormalizer`](artifician.processors.md#artifician.processors.normalizer.PathsNormalizer)
      * [`PathsNormalizer.get_path_values()`](artifician.processors.md#artifician.processors.normalizer.PathsNormalizer.get_path_values)
      * [`PathsNormalizer.normalize()`](artifician.processors.md#artifician.processors.normalizer.PathsNormalizer.normalize)
    * [`PropertiesNormalizer`](artifician.processors.md#artifician.processors.normalizer.PropertiesNormalizer)
      * [`PropertiesNormalizer.normalize()`](artifician.processors.md#artifician.processors.normalizer.PropertiesNormalizer.normalize)
    * [`StrategySelector`](artifician.processors.md#artifician.processors.normalizer.StrategySelector)
      * [`StrategySelector.get_key_values_delimiter()`](artifician.processors.md#artifician.processors.normalizer.StrategySelector.get_key_values_delimiter)
      * [`StrategySelector.get_paths_delimiter()`](artifician.processors.md#artifician.processors.normalizer.StrategySelector.get_paths_delimiter)
      * [`StrategySelector.get_properties_delimiter()`](artifician.processors.md#artifician.processors.normalizer.StrategySelector.get_properties_delimiter)
      * [`StrategySelector.select()`](artifician.processors.md#artifician.processors.normalizer.StrategySelector.select)
  * [artifician.processors.processor module](artifician.processors.md#module-artifician.processors.processor)
    * [`Processor`](artifician.processors.md#artifician.processors.processor.Processor)
      * [`Processor.process()`](artifician.processors.md#artifician.processors.processor.Processor.process)
      * [`Processor.subscribe()`](artifician.processors.md#artifician.processors.processor.Processor.subscribe)
  * [Module contents](artifician.processors.md#module-artifician.processors)

## artifician.dataset module

### *class* artifician.dataset.Dataset

Bases: `object`

Dataset contains all the functionality for preparing artifician data
: Dataset has events which are observed by observers (for eg: FeatureDefiniton, Processor)
  All the processed artifician data is stored in datastore
  which is an object of Pandas dataframe

Attributes:
: cached (dictionary): {event: rx.core.observable.observable.Observable}
  datastore (pandas.core.frame.DataFrame): all the samples are stored in datastore
  PREPARE_DATASET (function): event
  POST_PROCESS (function): event

#### add_samples(samples)

add samples to the datastore.

Args:
: samples (any): artifician data

Return:
: datastore (pandas.core.frame.DataFrame): dataset

#### observe(event)

build and return observable for given event. This method is
: called by the observer who wants to listen to the particular event.

Args:
: event (function): function to create observable from

Returns:
: observable (rx.core.observable.observable.Observable): Observable

#### post_process()

This event should be called after artifician data is prepared.
All the actions that needs to performed collectively on the whole
dataset should listen to post_process event.

## artifician.feature_definition module

### *class* artifician.feature_definition.FeatureDefinition(extractor=<function FeatureDefinition.<lambda>>, \*extractor_parameters)

Bases: `object`

Contains all the functionality for preparing single feature

Attributes:
: value (any): value of the feature
  cached (dictionary): {event: rx.core.observable.observable.Observable}
  extractor (function): extract feature value from the artifician
  EVENT_PROCESSED (function): event that processes the feature
  MAP_VALUES (function): event that maps values of feature
  extractor_parameters (
  <br/>
  ```
  *
  ```
  <br/>
  args): parameters for extractor function

#### map(feature_value)

Map the feature value from into int or list of int

Args:
: feature_value (any): feature value that needs to be mapped

Return:
: None

#### observe(event)

build and return observable for given event

Args:
: event (function): function to create observable from

Return:
: observable (rx.core.observable.observable.Observable): Observable

#### process(publisher, sample)

process the sample to build feature value
process should contain all the logic for completely processing the feature value

Args:
: sample (any): sample data
  publisher (object): instance of publisher

Return:
: feature_processed (list): processed feature_raw

#### subscribe(publisher, pool_scheduler=None)

Defines logic for subscribing to an event in publisher

Args:
: publisher (object): publisher instance
  pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

Return:
: None
