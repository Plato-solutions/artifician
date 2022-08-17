from pytest_bdd import scenario, given, when, then, parsers
import pytest
import ast
from artifician.processors.mapper import *
from artifician.dataset import Dataset
from artifician.feature_definition import FeatureDefinition


@given("We have dummy dataset and feature_definition objects created")
def step_impl():
    pytest.dataset = Dataset()
    pytest.feature_definition = FeatureDefinition(lambda x: x)
    pytest.feature_definition.subscribe(pytest.dataset)
    pytest.mapper = Mapper(FeatureMap())
    pytest.mapper.subscribe(pytest.feature_definition)


@scenario("features/mapper.feature", "mapper with single element and single feature map (map_keys = False)")
def test_string_mapper():
    print("single string mapper - testcase passed")


@given(parsers.parse("we are given single string as a {input_string} to map"))
def step_impl(input_string):
    pytest.input_string = input_string.strip('"')


@when("we try to map values to numbers")
def step_impl():
    samples = [pytest.input_string]
    pytest.datastore = pytest.dataset.add_samples(samples)


@then(parsers.parse("We should get {output} as output"))
def step_impl(output):
    assert pytest.datastore.iloc[-1, 1] == int(output)


@scenario("features/mapper.feature", "mapper with list of values only and a single feature map (map_keys = False)")
def test_string_list():
    print("list of strings - testcase passed ")


@given(parsers.parse("We are given lists of string as a {input_string} to map"))
def step_impl(input_string):
    pytest.input_string = ast.literal_eval(input_string)


@scenario("features/mapper.feature", "mapper with list of key values and single feature map (map_keys = False)")
def test_values_only():
    print("test values only - testcase passed")


@given(parsers.parse("we are given list of key value pair as a {input_string} where only values should be mapped"))
def step_impl(input_string):
    pytest.input_string = ast.literal_eval(input_string)


@scenario("features/mapper.feature", "mapper with list of key values and single feature map (map_keys = True)")
def test_key_values_list():
    print("key values string list - testcase passed")


@given(parsers.parse("We are given list of key values pair as a {input_string} to map"))
def step_impl(input_string):
    pytest.dataset = Dataset()
    pytest.feature_definition = FeatureDefinition(lambda x: x)
    pytest.feature_definition.subscribe(pytest.dataset)
    pytest.mapper = Mapper(FeatureMap(), map_key_values=True)
    pytest.mapper.subscribe(pytest.feature_definition)
    pytest.input_string = ast.literal_eval(input_string)


@when("we try to map list of values to numbers")
def step_impl():
    pytest.sample = [pytest.input_string]
    pytest.datastore = pytest.dataset.add_samples(pytest.sample)


@then(parsers.parse("We should get list of integers as a {output}"))
def step_impl(output):
    temp = pytest.datastore.iloc[-1, 1]
    assert pytest.datastore.iloc[-1, 1] == ast.literal_eval(output)
