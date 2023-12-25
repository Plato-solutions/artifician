
<div id="top"></div>  

[![codecov](https://codecov.io/gh/Plato-solutions/artifician/branch/main/graph/badge.svg?token=de0f5b64-eda8-4352-9d4d-48af50af44bb)](https://codecov.io/gh/Plato-solutions/artifician)
![CI/CD](https://github.com/Plato-solutions/artifician/actions/workflows/python-ci.yml/badge.svg?branch=main)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Plato-solutions/artifician)
[![PyPI version](https://badge.fury.io/py/artifician.svg)](https://pypi.org/project/artifician/)
[![GitBook](https://img.shields.io/badge/docs-GitBook-blue)](https://plato-solutions.gitbook.io/artifician/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Conda](https://anaconda.org/plato_solutions/artifician/badges/version.svg)](https://anaconda.org/plato_solutions/artifician)

  
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
url_domain = FeatureDefinition(extract_domain_name, dataset) # initializing feature_definition and passing extractor function name as a parameter and subscribing it to dataset
normalizer = Normalizer(PropertiesNormalizer(), url_domain delimiter = {'delimiter': ["."]})  # Initializing normalizer (processor) and passing properties normalizer as a parameter and subscribing it to url_domain
  
  
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