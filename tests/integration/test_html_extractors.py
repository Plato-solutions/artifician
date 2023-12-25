from artifician import Dataset, FeatureDefinition  # Replace with actual import
from bs4 import BeautifulSoup
from artifician.extractors.html_extractors import get_node_text, get_node_attribute, get_parent_node_text, get_child_node_text, count_child_nodes, get_sibling_node_text, get_parent_attribute, get_child_attribute
import pandas as pd
def test_integration_get_node_text():
    # Prepare the dataset
    dataset = Dataset()
    
    # Create the feature definition
    feature_def = FeatureDefinition(get_node_text, [dataset])
    
    # Prepare sample HTML and create BeautifulSoup object
    sample_html = "<html><body><p>Test Text</p></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    
    # Add samples to dataset
    node = soup.find('p')
    dataset.add_samples([[node]])  # I'm assuming add_samples takes a list of samples, each being a list
    
    # Fetch the processed samples (pseudo-code, replace with actual method)
    processed_samples = dataset.datastore
    
    # Assert that the processed samples are as expected
    assert processed_samples.iloc[0,1] == "Test Text"


def test_integration_get_node_attribute():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_node_attribute, [dataset], "class")
    
    sample_html = "<html><body><p class='test_class'>Test Text</p></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('p')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "test_class"

def test_integration_get_parent_node_text():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_parent_node_text, [dataset])
    
    sample_html = "<html><body><p>Test Text</p></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('p')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "Test Text"

def test_integration_get_child_node_text():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_child_node_text, [dataset])
    
    sample_html = "<html><body><div><p>Child Text</p></div></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('div')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "Child Text"

def test_integration_count_child_nodes():
    dataset = Dataset()
    feature_def = FeatureDefinition(count_child_nodes, [dataset])
    
    sample_html = "<html><body><div><p>Child 1</p><p>Child 2</p></div></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('div')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == 2

def test_integration_get_sibling_node_text():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_sibling_node_text, [dataset])
    
    sample_html = "<html><body><p>Test Text</p><p>Sibling Text</p></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('p')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "Sibling Text"

def test_integration_get_parent_attribute():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_parent_attribute, [dataset], "id")
    
    sample_html = "<html><body><div id='parent_id'><p>Test Text</p></div></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('p')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "parent_id"

def test_integration_get_child_attribute():
    dataset = Dataset()
    feature_def = FeatureDefinition(get_child_attribute, [dataset], "class")
    
    sample_html = "<html><body><div><p class='child_class'>Child Text</p></div></body></html>"
    soup = BeautifulSoup(sample_html, 'html.parser')
    node = soup.find('div')
    
    dataset.add_samples([[node]])
    processed_samples = dataset.datastore
    assert processed_samples.iloc[0, 1] == "child_class"
