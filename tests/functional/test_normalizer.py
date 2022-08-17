from pytest_bdd import scenario, given, when, then, parsers
import pytest
import ast
from artifician.processors.normalizer import *


@scenario("features/normalizer.feature", "Properties Normalizer")
def test_properties_normalizer():
    print("Properties Normalizer - testcase passed")


@given(parsers.parse("we have {start} as a input string"))
def initialize_input(start):
    pytest.start = start.strip('"')


@when(parsers.parse('we use properties normalizer and " " as a delimiter'))
def initialize_normalizer():
    pytest.normalizer = PropertiesNormalizer()
    pytest.output = pytest.normalizer.normalize(pytest.start, delimiter={'delimiter': [' ']})


@then(parsers.parse("we should get {output} as normalized string"))
def match_output(output):
    expected_output = ast.literal_eval(output)
    assert pytest.output == expected_output


@scenario("features/normalizer.feature", "Paths Normalizer")
def test_paths_normalizer():
    print("Paths Normalizer - testcase passed")


@when(parsers.parse('we use paths normalizer and "/" as a delimiter'))
def initialize_normalizer():
    pytest.normalizer = PathsNormalizer()
    pytest.output = pytest.normalizer.normalize(pytest.start, delimiter={'delimiter': ['/']})


@scenario("features/normalizer.feature", "Key Values Normalizer")
def test_key_values_normalizer():
    print("Key Values Normalizer - testcase passed")


@when(parsers.parse('we use key normalizer normalizer "," as a delimiter and "=" as a assignment'))
def initialize_normalizer():
    pytest.normalizer = KeyValuesNormalizer()
    pytest.output = pytest.normalizer.normalize(pytest.start, {'delimiter': [","], 'assignment': '='})
