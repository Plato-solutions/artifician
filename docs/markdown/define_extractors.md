# Defining Custom Extractors

## Introduction

Extractors are user-defined functions that serve as the cornerstone for feature extraction in Artifician. This document provides an in-depth guide on how to create your own custom extractors.

## Why Custom Extractors?

There might be specific features you need to extract from your data that the pre-defined extractors do not cover. In such cases, custom extractors come in handy.

## How Extractors Work

Extractors operate by taking a sample of raw data and extracting specific features from it. These extracted features are then passed on to the FeatureDefinition for further processing.

## Example of a Simple Extractor

Here is an example that extracts domain names from URLs.

```python
def extract_domain_name(sample):
    domain_name = sample.split("//")[-1].split('/')[0]
    return domain_name
```

## Integrating Custom Extractors

To use your custom extractor, pass it as an argument when initializing a FeatureDefinition object.

```python
url_domain = FeatureDefinition(extract_domain_name)
```

## Advanced Usage

If your feature extraction is more complex and involves multiple steps, you can also create a class-based extractor. This allows for more modularity and reusability.

```python
class AdvancedExtractor:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def extract(self, sample):
        # Complex extraction logic here
        return extracted_feature

advanced_extractor = AdvancedExtractor(param1_value, param2_value)
advanced_feature = FeatureDefinition(advanced_extractor.extract)
```

## Conclusion

Custom extractors offer a flexible way to handle feature extraction specific to your needs. They seamlessly integrate with the existing components of Artifician, allowing for a cohesive and streamlined feature extraction process.