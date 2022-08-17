Feature: Mapper

  Background:
    Given We have dummy dataset and feature_definition objects created

  Scenario Outline: mapper with single element and single feature map (map_keys = False)
    Given we are given single string as a <input_string> to map
    When we try to map values to numbers
    Then We should get <output> as output

    Examples:
    | input_string   | output |
    | "hello"        |    0   |
    | "world"        |    1   |
    | "hello"        |    0   |


  Scenario Outline: mapper with list of values only and a single feature map (map_keys = False)
    Given We are given lists of string as a <input_string> to map
    When we try to map list of values to numbers
    Then We should get list of integers as a <output>

    Examples:
    | input_string                | output           |
    | ["hello", "world"]          |    [0,1]         |
    | ["world", "is", "good"]     |    [1,2,3]       |
    | ["it", "is", "not", "good"] |    [4,2,5,3]     |


  Scenario Outline: mapper with list of key values and single feature map (map_keys = False)
    Given we are given list of key value pair as a <input_string> where only values should be mapped
    When we try to map list of values to numbers
    Then We should get list of integers as a <output>

    Examples:
    | input_string                   | output   |
    | [("hello", "world")]           | [0]      |
    | [("hello", "universe")]        | [0]      |
    | [("universe", "hello")]        | [6]      |

  Scenario Outline: mapper with list of key values and single feature map (map_keys = True)
    Given We are given list of key values pair as a <input_string> to map
    When we try to map list of values to numbers
    Then We should get list of integers as a <output>

    Examples:
    | input_string                                  | output   |
    | [("hello", "world")]                          | [7]      |
    | [("hello", "world")]                          | [7]      |
    | [("hello", "universe")]                       | [8]      |

