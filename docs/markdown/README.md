# Introduction

## “Turn your data preparation nightmares into a dream.”

In the world of Artificial Intelligence and Machine Learning, data is the new oil. However, this data often comes in raw, unstructured formats that need extensive cleaning and transformation to be usable. This preprocessing phase can be a grueling task, taking up to 80% of a data scientist’s or ML engineer’s time.

Artifician aims to revolutionize this crucial yet tedious step. It is an event-driven framework specifically designed to simplify and speed up the process of dataset preparation for AI and ML models. Whether you’re dealing with text, numbers, or more complex data types, Artifician offers a streamlined, efficient way to get your data model-ready.

## Key features of Artifician ?

- **Time-Saving**: Reduces dataset preparation time by up to 50%, freeing you to focus on model building and fine-tuning.
- **Efficient Code**: Minimizes the lines of code you need to write, making your development process leaner and faster.
- **Readability and Manageability**: Ensures that your code is not just functional but also clean, well-organized, and easy to understand, even for those who didn’t write it.
- **CPU Concurrency**: Fully utilizes your CPU capabilities to perform data preparation tasks in parallel, significantly speeding up the process.

---

## Simple Example

Let’s take a simple example to understand the impact of Artifician.
Here we will take URLs as the raw data and try to extract the directory path of the URL
and convert it to numerical format while maintaining the sequential information.

## Without Artifician

```python
   import re
   import string
   from nltk.tokenize import word_tokenize
   from nltk.corpus import stopwords
   from nltk.stem import PorterStemmer

   sample_texts = [
       "Love this product! Absolutely fantastic.",
       "Hated the experience. Terrible service!"
   ]

   def clean_text(text):
       text = re.sub(r'\d+', '', text)  # Remove numbers
       text = text.translate(str.maketrans('', '', string.punctuation)) # Remove punctuation
       text = text.lower()  # Convert to lowercase
       return text

   def remove_stopwords(tokens):
       stop_words = set(stopwords.words('english'))
       return [word for word in tokens if word not in stop_words]

   processed_texts = []
   for text in sample_texts:
       cleaned = clean_text(text)
       tokenized = word_tokenize(cleaned)
       no_stopwords = remove_stopwords(tokenized)

   print(no_stopwords)
```

Now let’s prepare the same dataset using Artifician

## Using Artifician

```python
   from artifician import Dataset, FeatureDefinition
   from artifician.processors import *

   def get_text(text): return text

   sample_texts = [
       "Love this product! Absolutely fantastic.",
       "Hated the experience. Terrible service!"
   ]

   dataset = Dataset()
   feature = FeatureDefinition(get_text, [dataset])
   pipeline = TextCleaningProcessor().then(TokenizationProcessor()).then(StopWordsRemoverProcessor())
   pipeline.subscribe(feature)

   prepared_data = dataset.add_samples(sample_texts)
   print(prepared_data)
```

The traditional method for text data preparation involves multiple,
disjointed steps with separate handling for cleaning, tokenizing, and
removing stopwords, resulting in a longer and more complex code.
Artifician streamlines this process significantly with its Processor
Chain Manager. It encapsulates these steps into a cohesive pipeline,
reducing code length and complexity. This approach not only simplifies
coding but also enhances maintainability and data flow efficiency,
showcasing Artifician’s advantage in creating more intuitive and
error-resistant data processing workflows.


## Output
| Original Text                            | Processed Text                                 |
|------------------------------------------|------------------------------------------------|
| Love this product! Absolutely fantastic. | ['love', 'product', 'absolutely', 'fantastic'] |
| Hated the experience. Terrible service!  | ['hate', 'experience', 'terrible', 'service']  |
