from bs4 import BeautifulSoup
from artifician import *
from artifician.extractors.html_extractors import get_node_attribute

def test_processor_chain_with_init_method():
    html_elements = BeautifulSoup("""<div class="container"> <p class="Hello World">Hello</p>
                    <span class="Hello value">John</span> </div> """, "html.parser").find_all()

    dataset = Dataset()
    feature = FeatureDefinition(get_node_attribute, [dataset],  "class")

    text_normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': [" "]})
    mapper = Mapper(feature_map=FeatureMap({"": 0}))

    processor_chain = chain([text_normalizer, mapper])

    processor_chain.subscribe(feature)
    expected_ouput = [[1], [2,3], [2,4]]
    datastore = dataset.add_samples(list(html_elements))
    assert expected_ouput == list(datastore[1].values)

def test_processor_chain_with_then_method():
    html_elements = BeautifulSoup("""<div class="container"> <p class="Hello World">Hello</p>
                    <span class="Hello value">John</span> </div> """, "html.parser").find_all()

    dataset = Dataset()
    feature = FeatureDefinition(get_node_attribute, [dataset],  "class")

    text_normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': [" "]})
    mapper = Mapper(feature_map=FeatureMap({"": 0}))

    chain = text_normalizer.then(mapper)

    chain.subscribe(feature)
    expected_ouput = [[1], [2,3], [2,4]]
    datastore = dataset.add_samples(list(html_elements))
    assert expected_ouput == list(datastore[1].values)