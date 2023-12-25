Feature: Normalizer
    Scenario Outline: Properties Normalizer
        Given we have <start> as a input string
        When we use properties normalizer and " " as a delimiter
        Then we should get <output> as normalized string

        Examples:
        | start                               | output                                                                     |
        |  "Advanced Reports for Magento 2"   |  [('Advanced', 0), ('Reports', 1), ('for', 2), ('Magento', 3), ('2', 4)]   |
        |  ""                                 |  [('', 0)]                                                                 |


    Scenario Outline: Paths Normalizer
        Given we have <start> as a input string
        When we use paths normalizer and "/" as a delimiter
        Then we should get <output> as normalized string

        Examples:
        | start             | output                                                 |
        |  "/body/div/div"  | [('body/', 0), ('body/div/', 1), ('body/div/div/', 2)] |
        |  ""               | []                                                     |


    Scenario Outline: Key Values Normalizer
        Given we have <start> as a input string
        When we use key normalizer normalizer "," as a delimiter and "=" as a assignment
        Then we should get <output> as normalized string

        Examples:
        | start                                  | output                                              |
        |  "width=device-width,initial-scale=1"  | [("device-width", "width"), ("1", "initial-scale")] |
        |  ""                                    | []                                                  |