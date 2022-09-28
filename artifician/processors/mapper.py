"""
   Copyright 2021 Plato Solutions, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
from . import processor


class Mapper(processor.Processor):
    """Mapper is a processor responsible for mapping/converting feature values to int

    Attributes:
        feature_map (FeatureMap): Feature map contains dictionary --> {value: id}
        map_key_values (bool): True ---> Map both key and value, False ---> map only keys
    """

    def __init__(self, feature_map, map_key_values=False):
        """initialise Mapper by setting up the feature map

        Args:
            feature_map (FeatureMap): instance of feature_map
            map_key_values (Boolean):  True = map both the key and values, False = map only values
        """
        self.feature_map = feature_map
        self.map_key_values = map_key_values

    def process(self, publisher, feature_value):
        """update the feature value of the publisher by mapping features value to int

        Args:
            publisher (object): instance of the publisher
            feature_value(string): feature_value

        Returns:
            value_id =
        """

        value_id = []
        if isinstance(feature_value, str) or len(feature_value) == 0:
            value_id = self.feature_map.get_value_id(feature_value)
        else:
            for value in feature_value:
                if self.map_key_values is True or isinstance(value, str):
                    value_id.append(self.feature_map.get_value_id(value))
                else:
                    value_id.append(self.feature_map.get_value_id(value[0]))

        publisher.value = value_id

    def subscribe(self, publisher, pool_scheduler=None):
        """Defines logic for subscribing to an event in publisher

        Args:
            publisher (object): instance of publisher

            pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

        Return:
            None
        """

        observable = publisher.observe(publisher.MAP_VALUES)
        observable.subscribe(lambda feature_raw: self.process(publisher, feature_raw),
                             scheduler=pool_scheduler)


class FeatureMap:
    """Converts given value to int

    Attributes:
        values_map (dictionary): {value : id}
    """

    def __init__(self, values_map={}):
        self.values_map = values_map

    def get_value_id(self, value):
        """returns the id of the value in values. convert any datatype to str as
        dictionary keys can not be of other than str and int. each format can be
        converted to str only.

        Args:
            value (any): value

        Return:
            value_id (int):  ID of the value
        """
        value = str(value)

        if value not in self.values_map.keys():
            value_id = len(self.values_map)
            self.values_map[value] = value_id
        else:
            value_id = self.values_map[value]

        return value_id
