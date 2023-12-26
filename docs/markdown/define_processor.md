# Defining Custom Processors

## Introduction

In Artifician, processors play a crucial role in transforming raw data into features that can be used by machine learning models. While the library offers a wide variety of built-in processors, there are scenarios where you may need to define your own. This guide walks you through that process.

## Why Custom Processors?

Built-in processors cover a broad range of common use-cases, but they can’t cater to every specific need. Custom processors allow you to define your own logic for data transformation, giving you the flexibility to handle any unique requirements your project may have.

## How Processors Work

A processor subscribes to a publisher (usually a FeatureDefinition or Dataset object) and listens for specific events. When the event is triggered, the processor’s process method is called, which then applies your custom logic to the feature data.

## Example of a Simple Processor

Here’s a simple example that doubles the input value.

```python
from . import Processor

class DoubleValueProcessor(Processor.processor):
    def process(self, publisher, value):
        publisher.value = value * 2

    def subscribe(self, publisher, pool_scheduler=None):
        observable = publisher.observe(publisher.EVENT_PROCESSED)
        observable.subscribe(lambda value: self.process(publisher, value), scheduler=pool_scheduler)
```

## Integrating Custom Processors

After defining a custom processor, you can easily integrate it into your data pipeline as you would with any built-in processor.

```python
my_custom_processor = DoubleValueProcessor()
my_custom_processor.subscribe(my_feature_definition)
```

## Advanced Usage

For more advanced scenarios, you can make your processor stateful, make use of the pool_scheduler for parallel processing, or even chain multiple processors together. The possibilities are limitless.

## Conclusion

Custom processors provide the flexibility to handle any data transformation logic your project requires. They can be as simple or as complex as needed, and seamlessly integrate into the Artifician framework.