
<div id="top"></div>  
  
<!-- PROJECT LOGO -->  
  
<br />  
  
<div align="center">  
  
<a href="https://www.platosolutions.io/">  
  
<img src="https://i.ibb.co/w4v9g9d/Plato-Logo.png" alt="Logo" />  
    
</a>  
  
<h1 align="center">Artifician</h1>  
  
<p align="center">  
  
Artifician is an event driven library developed to simplify and speed up the process of preparation of the datasets for Artificial Intelligence models.
  
<br />  

</div>

# Getting Started
  
## Pre-requisites  
- [**python**](https://www.python.org/) **v3.6** or later

## Installation 
Binary installers for the latest released version are available at the Python Package Index (PyPI) and on Conda

```sh
# or PyPI
pip install artifician
```

```sh
# conda
conda install -c plato_solutions artifician
```

## Documentation
Please visit [Aritfician Docs](https://plato-solutions.gitbook.io/artifician/)
  
## Usage  
  
```python  
from artifician.dataset import *
from artifician.feature_definition import *
from artifician.processors.normalizer import *

  
def extract_domain_name(sample):  
    """function for extracting the path from the given URL"""
    domain_name = sample.split("//")[-1].split('/')[0] 
 
    return domain_name  
 
input_data = ['https://www.google.com/', 'https://www.youtube.com/']  
  
dataset = Dataset() # initializing dataset object
url_domain = FeatureDefinition(extract_domain_name) # initializing feature_definition and passing extractor function name as a parameter 
normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': ["."]})  # Initializing normalizer (processor)
  
""" Now let's set up the connections, we can do that using subscribe method. listener subscribes to the event to which he wants to 
listen to. In following example normalizer subscribes to url_domain feature that means everytime url_domain is processed normalizer 
will listen to it and perform its execution. Similarly in the case of url_doamin and dataset, here url_domain is listening to datatset. """ 

normalizer.subscribe(url_domain) 
url_domain.subscribe(dataset)  
  
""" Now we are all set to go, all we have to do is call add_samples method on the dataset object and pass the input data
after calling the add_samples, url_domain will start its execution and extract the data using extract_domain_name function, as soon url_domain
feature is processed normalizer will start it execution and furthur is will process the data extracted by url_domain. The processed data is then
passed back to the dataset. Following diagram will make it more clear for you. """ 

prepared_data = dataset.add_samples(input_data)  
print(prepared_data)  
  
```  
  
Output  
|  |                        0 |                                 1  |  
|--|--------------------------|------------------------------------|  
|0 | https://www.google.com/  | [(www, 0), (google, 1), (com, 2)] |  
|1 | https://www.youtube.com/ | [(www, 0), (youtube, 1), (com, 2)] |