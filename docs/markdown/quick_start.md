# Quick Start

Let’s break down the simple code example to fully understand the working of the library.

---

## Define Extractor

First of all, we define the extractor function to extract feature value from the sample data.
Extractor function could be anything which extracts information from given raw data.
As in this case extractor extracts the domain name from the url.

```default
def extract_domain_name(sample):
    domain_name = sample.split("//")[-1].split('/')[0]
return domain_name
```

## Initialize components

Next, we simply initialize the Dataset , FeatureDefinition and Processor object which is the normalizer in this case.
We need to pass the extractor function as the parameter while initializing the FeatureDefinition object.
Normalizer is just one of the Processor which helps in processing the extracted feature data. 
In this we pass dataset object to the feature definition so that it subscribes to the dataset. and whenever dataset.add_samples
method is called it will trigger the process method of the FeatureDefinition.
similarly, we pass the FeatureDefinition object to the normalizer so that it subscribes to the FeatureDefinition and whenever
FeatureDefinition.process method is called it will trigger the process method of the normalizer.

```default
dataset = Dataset()
url_domain = FeatureDefinition(extract_domain_name, [dataset])
normalizer = Normalizer(PropertiesNormalizer(), [url_domain], delimiter = {'delimiter': ["."]})
``` 

## Dataset Preparation

That’s all now we simply define the sample data from which dataset will be prepared,
lastly call the dataset.add_samples method and pass the sample data.

```default
sample_data = ['https://www.google.com/', 'https://www.youtube.com/']
prepared_data = dataset.add_samples(sample_data)
print(prepared_data)
```

Now you might be wondering how did the url_domain and the normalizer got executed as we only called the add_samples method
on dataset. Well, when url_domain(FeatureDefinition) subscribes to dataset (url_domain.subscribe(dataset))
what happens behind the scenes is url_domain starts listening to the add_samples method of the dataset,
now whenever add_samples method is called url_domain will notice it and it will trigger process method of its own.
Similarly, as normalizer(Processor) subscribes to url_domain it starts listening to process method of the url_domain.
and whenever process method of the FeatureDefinition is called Processor executes it own process method.

---

## Output

|    | 0                                                    | 1                                  |
|----|------------------------------------------------------|------------------------------------|
|  0 | [https://www.google.com/](https://www.google.com/)   | [(www, 0), (google, 1), (com, 2)]  |
|  0 | [https://www.youtube.com/](https://www.youtube.com/) | [(www, 0), (youtube, 1), (com, 2)] |