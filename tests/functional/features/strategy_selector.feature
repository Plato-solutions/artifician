
Feature: StrategySelector
  Automatically select the best normalizer strategy to normalize the text

  Scenario Outline:  Checking strategy selector with different kinds of paths strings
    Given we are given strings as a <input_text>
    When we try to identify the appropriate normalizer strategy to normalize the text
    Then we should get <delimiter> as output

    Examples:
    |input_text                         | delimiter                             |
    |"a/b/c"                            | {"delimiter":"/"}                     |
    |"a/b"                              | {"delimiter":"/"}                     |
    | ["a/b/c", "a/b", "a/b/c/d"]       | {"delimiter":"/"}                     |
    |"a=b"                              | {"delimiter": " ", "assignment": "="} |
    |"a=b&b=c"                          | {"delimiter": "&", "assignment": "="} |
    |"a=b&b=c"                          | {"delimiter": "&", "assignment": "="} |
    |["a=b&b=c", "a=b", "&a=b&b=c&c=d"] | {"delimiter": "&", "assignment": "="} |
    |["a:b&b:c", "a:b", "&a:b&b:c&c:d"] | {"delimiter": "&", "assignment": ":"} |
    |["a:b,b:c", "a:b", "a:b,b:c,c:d"]  | {"delimiter": ",", "assignment": ":"} |
    | "a b c"                           | {"delimiter": " "}                      |
    | "a,b,c,d"                         | {"delimiter": ","}                      |
    | ["a b,c", "a b c,d"]              | {"delimiter": " "}                      |
    | "a-b-c-d"                         | {"delimiter": "-"}                      |
    | "a_b_d"                           | {"delimiter": "_"}                      |
    | "a b-c,d"                         | {"delimiter": "-"}                      |





