# artifician.processors.processor module


### _class_ artifician.processors.processor.Processor()
Bases: `abc.ABC`

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
