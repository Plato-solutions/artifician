# Introduction

Preparing dataset for AI (Artificial Intelligence) models is a difficult and a time-consuming job.
A typical ML engineer spends days, weeks and sometimes months preparing the dataset. With the help
of Artifician library developers will be able to prepare dataset in very less time.

Artifician is an event driven framework developed to simplify and speed up the process of preparation
of the datasets for AI models. Artifician contains predefined set of processors for converting unstructured
data into structured data. You can use them or define your own if you don’t find the one that fulfill your needs.
The ultimate aim is to have as many as processors that developers will no longer need to define any new processors.

Key features of Artifician:


* Saves up to 50% of time


* Fewer lines of code


* Makes code more readable and easy to manage


* CPU Concurrency


---

## Simple Example

Let’s take a simple example to understand the impact of the Artifician.
Here will take urls as the raw data and try to extract the directory path of the url
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

Here you can notice how each and every function is tightly coupled to each other and a single change will
lead to changes in several other places. This code is just for preparing a single feature.
Just imagine the level of complexity when writing code for preparing tens and hundreds of features.

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

Artifician library decouples all the entities and hence makes it very easy to manage.
You can add, remove and update features very easily without worrying about anything else.
Here we used normalizer and mapper which are inbuilt processors in artifician library.

## Output

| index  | 0  | 1            | 
|---     | -- | ------------ |
| 0      | [https://www.example.com/path/path1/path2](https://www.example.com/path/path1/path2) | [0, 1, 2]    |
| 1      | [https://www.example.com/path/path1/path2/path3](https://www.example.com/path/path1/path2/path3) | [0, 1, 2, 3] |
