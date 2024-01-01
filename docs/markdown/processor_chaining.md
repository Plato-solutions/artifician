# Processor Chaining for Streamlined Data Operations in Artifician

## Overview

Discover Processor Chaining – a fundamental concept in the Artifician library that revolutionizes the way you handle data processing workflows. Whether it's complex data transformations, in-depth text analysis, or sequential data manipulations, Processor Chaining is the conceptual backbone that ensures smooth and efficient operations. It's a versatile approach, applicable not only to NLP tasks but to a wide array of sequential data operations.

## Key Features

- **Sequential Execution**: Processor Chaining provides a structured way to pass data through a series of processors, maintaining a logical and efficient flow.
- **Flexible Pipeline Construction**: Adapt your data processing pipeline to your project's evolving requirements by adding, removing, or rearranging processors.
- **Broad Applicability**: This concept is compatible with a diverse range of processors, making it an ideal choice for managing complex data workflows.

## Syntax Showcase

Processor chaining can be achieved in two different ways:

- **Chain Processors with `.then()`**:
  ```python
   pipeline = TextCleaningProcessor().then(TokenizationProcessor()).then(StemLemProcessor())
  ```
This approach lets you link processors together in a logical sequence, ideal for step-by-step construction of a pipeline.

- **Chain Processors with `.then()`, Using Lists**:
  ```python
  pipeline = TextCleaningProcessor().then([TokenizationProcessor(), StemLemProcessor()])
  ```
This method enhances flexibility, enabling you to add multiple processors at once using a list - perfect for incorporating groups of processors efficiently.

## Example Scenario: NLP Processing Pipeline

Imagine you're preparing textual data for NLP analysis. The raw data requires cleaning, tokenizing, stemming or lemmatizing, and stop word removal. Processor Chaining simplifies this daunting task, allowing seamless integration of these steps into an effective pipeline.

Now, let's see how you can effortlessly achieve this with processor chaining.

## Building an NLP Pipeline with PCM

Here's how Processor Chaining can be used to create a comprehensive NLP processing pipeline:

```python
from artifician import Dataset, FeatureDefinition
from artifician.processors import *

# Initialize individual processors
cleaner = TextCleaningProcessor()
tokenizer = TokenizationProcessor(method='word')
stemlem = StemLemProcessor()
stopword = StopWordsRemoverProcessor()

# Define a extractor to retrieve text
def get_text(text): return text

# Sample texts for processing
sample_texts = [
    "The quick brown fox jumps over the lazy dog!",
    "<p>HTML tags should be removed.</p>",
]

# Setup Dataset and FeatureDefinition
dataset = Dataset()
feature = FeatureDefinition(get_text, [dataset])

# Create and configure the processing pipeline
processing_pipeline = cleaner.then(tokenizer).then(stemlem).then(stopword)
processing_pipeline.subscribe(feature)

# Process the sample texts
datastore = dataset.add_samples(sample_texts)
```

### Output

After running our NLP pipeline with processor chaining, we successfully process the text samples, which results in a neatly organized DataFrame. The DataFrame showcases a side-by-side comparison of the original texts and their processed counterparts, illustrating the effectiveness of our processing pipeline:

| Original Text                                    | Processed Text                         |
|--------------------------------------------------|----------------------------------------|
| The quick brown fox jumps over the lazy dog!     | ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog'] |
| <p>The HTML tags should be removed.</p>          | ['html', 'tag', 'remove']              |