# Processor Chain Manager: Your Data Operations Conductor

## Overview

Meet the Processor Chain Manager (PCM) – a core component of the Artifician library designed to bring order and efficiency to your data processing workflows. Whether you're handling complex data transformations, diving into text analysis, or orchestrating a series of data manipulations, PCM is here to ensure everything runs in a smooth, sequential manner. It's not just an asset for NLP tasks; it's a versatile tool for any sequential data operation you can imagine.

## Key Features

- **Sequential Execution**: PCM ensures a smooth transition of data from one processor to the next, maintaining a logical flow in your data processing tasks.
- **Flexible Pipeline Construction**: Add, remove, or rearrange processors in your pipeline as your project's needs evolve.
- **Broad Applicability**: Compatible with a diverse range of processors, PCM is your go-to for managing complex data workflows.

## Syntax Showcase

PCM offers two intuitive ways to build your processing chain:

- **Chain Processors with `.then()`**:
  ```python
   pipeline = TextCleaningProcessor().then(TokenizationProcessor()).then(StemLemProcessor())
  ```
This approach lets you elegantly link processors in a 'do this, then that' fashion. It's a great way to build a pipeline from scratch, or to add new processors to an existing pipeline.

- **Initialize with a List of Processors**:
  ```python
  processors = [TextCleaningProcessor(), TokenizationProcessor(), StemLemProcessor()]
  pipeline = ProcessorChainManager(processors)
  ```
Here, you set up your processors first and then hand them over to PCM. This is a great way to build a pipeline from a list of existing processors.


## Example Scenario: NLP Processing Pipeline

Imagine you're tasked with preparing textual data for NLP analysis. The raw data needs cleaning, tokenizing, stemming or lemmatizing, and finally, removing unnecessary stop words. This can be a daunting series of tasks, requiring precise coordination between different processing steps. This is where the Processor Chain Manager (PCM) becomes your ally, enabling you to seamlessly integrate these steps into a cohesive and efficient pipeline.

Now, let's see how you can effortlessly achieve this with the PCM.

## Building an NLP Pipeline with PCM

Here's a practical demonstration of using PCM to create a comprehensive NLP processing pipeline:

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

After running our NLP pipeline with PCM, we successfully process the text samples, which results in a neatly organized DataFrame. The DataFrame showcases a side-by-side comparison of the original texts and their processed counterparts, illustrating the effectiveness of our processing pipeline:

| Original Text                                    | Processed Text                         |
|--------------------------------------------------|----------------------------------------|
| The quick brown fox jumps over the lazy dog!     | ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog'] |
| <p>The HTML tags should be removed.</p>          | ['html', 'tag', 'remove']              |

This output demonstrates PCM's ability to transform raw text into a format that's ready for advanced NLP tasks, all done seamlessly and efficiently. 