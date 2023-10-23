# Introduction

## “Turn your data preparation nightmares into a dream.”

In the world of Artificial Intelligence and Machine Learning, data is the new oil. However, this data often comes in raw, unstructured formats that need extensive cleaning and transformation to be usable. This preprocessing phase can be a grueling task, taking up to 80% of a data scientist’s or ML engineer’s time.

Artifician aims to revolutionize this crucial yet tedious step. It is an event-driven framework specifically designed to simplify and speed up the process of dataset preparation for AI and ML models. Whether you’re dealing with text, numbers, or more complex data types, Artifician offers a streamlined, efficient way to get your data model-ready.

Key features of Artifician:

## Why Artifician?

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

```default
sample_data = ['https://www.example.com/path/path1/path2', 'https://www.example.com/path/path1/path2/path3']
path_map = []

def extract_path(url):

    url_path = urlparse(url).path

    if url_path.endswith('html'):
        url_path = '/'.join(url_path.split('/')[:-1])

    return url_path

def normalize_path(url_path, delimiter):

    url_path = re.split(f'{delimiter}', url_path)[1:]

    return url_path

def map_path_values(url_path):

    path_values_map = []

    for path in url_path:
        if path not in path_map:
            path_map.append(path)

        path_values_map.append(path_map.index(path))

    return path_values_map

dataset = pd.DataFrame()

for sample in sample_data:
    path = extract_path(sample)
    normalized_path = normalize_path(path, '/')
    mapped_path = map_path_values(normalized_path)
    sample_data = [sample, mapped_path]
    dataset = dataset.append(pd.Series(sample_data), ignore_index=True)

print(dataset)
```

As you can notice, each function in the above code is tightly coupled, making it prone to errors and difficult to manage. Now, let’s see how Artifician simplifies this.es.

Now let’s prepare the same dataset using Artifician

## Using Artifician

```default
from urllib.parse import urlparse
from artifician import *
from artifician.Processors import *


def extract_path(url):
    url_path = urlparse(url).path

    if url_path.endswith('html'):
        url_path = '/'.join(url_path.split('/')[:-1])

    return url_path


sample_data = ['https://www.example.com/path/path1/path2', 'https://www.example.com/path/path1/path2/path3']

dataset = Dataset.Dataset()
url_domain = FeatureDefinition.FeatureDefinition(extract_path)
normalizer = Normalizer(PathsNormalizer(), delimiter={'delimiter': ["/"]})
mapper = Mapper.Mapper(Mapper.FeatureMap())

normalizer.subscribe(url_domain)
mapper.subscribe(url_domain)
url_domain.subscribe(dataset)

prepared_data = dataset.add_samples(sample_data)
print(prepared_data)
```

Artifician library decouples all the entities, making your codebase much easier to manage. You can add, remove, and update features effortlessly, without affecting other parts of your code.

## Output

|    | 0                                                                                                | 1            |
|----|--------------------------------------------------------------------------------------------------|--------------|
|  0 | [https://www.example.com/path/path1/path2](https://www.example.com/path/path1/path2)             | [0, 1, 2]    |
|  1 | [https://www.example.com/path/path1/path2/path3](https://www.example.com/path/path1/path2/path3) | [0, 1, 2, 3] |
