from pytest_bdd import scenario, given, when, then, parsers
import pytest
import ast
from artifician.processors.normalizer import StrategySelector, PathsNormalizer


@scenario("features/strategy_selector.feature", "Checking strategy selector with different kinds of paths strings")
def test_paths_string():
    print("strategy selector - testcase passed")


@given(parsers.parse("we are given strings as a {input_text}"))
def set_input_string(input_text):
    if type(input_text) == list:
        pytest.input_text = ast.literal_eval(input_text)
    else:
        pytest.input_text = input_text.strip('"')


@when(parsers.parse("we try to identify the appropriate normalizer strategy to normalize the text"))
def identify_strategy():
    strategy_selector = StrategySelector()
    pytest.selected_strategy, pytest.selected_delimiter = strategy_selector.select(pytest.input_text)


@then(parsers.parse("we should get {delimiter} as output"))
def check_output(delimiter):
    delimiter = ast.literal_eval(delimiter)
    assert pytest.selected_delimiter == delimiter


