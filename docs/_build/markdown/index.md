<!-- artifician documentation master file, created by
sphinx-quickstart on Sun Feb 20 23:06:29 2022.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Documentation


* [Introduction](intro.md)


    * [Simple Example](intro.md#simple-example)


    * [Without Artifician](intro.md#without-artifician)


    * [Using Artifician](intro.md#using-artifician)


    * [Output](intro.md#output)


* [Installation Guide](getting_started.md)


    * [Pre-requisites](getting_started.md#pre-requisites)


    * [Installation](getting_started.md#installation)


* [Quick Start](quick_start.md)


    * [Define Extractor](quick_start.md#define-extractor)


    * [Initialize components](quick_start.md#initialize-components)


    * [Subscriptions](quick_start.md#subscriptions)


    * [Dataset Preparation](quick_start.md#dataset-preparation)


    * [Output](quick_start.md#output)


* [Advanced Concepts](advanced_concepts.md)


    * [Defining new processor](define_processor.md)


    * [Library Architecture](library_architecture.md)


        * [Events](library_architecture.md#events)


        * [Dataset](library_architecture.md#dataset)


        * [Feature Definition](library_architecture.md#feature-definition)


        * [Processors](library_architecture.md#processors)


        * [RxPY](library_architecture.md#rxpy)


* [API](modules.md)


    * [artifician package](API.md)


        * [Subpackages](API.md#subpackages)


            * [artifician.processors package](artifician.processors.md)


                * [Submodules](artifician.processors.md#submodules)


                    * [artifician.processors.mapper module](artifician.processors.mapper.md)


                        * [`FeatureMap`](artifician.processors.mapper.md#artifician.processors.mapper.FeatureMap)


                            * [`FeatureMap.get_value_id()`](artifician.processors.mapper.md#artifician.processors.mapper.FeatureMap.get_value_id)


                        * [`Mapper`](artifician.processors.mapper.md#artifician.processors.mapper.Mapper)


                            * [`Mapper.process()`](artifician.processors.mapper.md#artifician.processors.mapper.Mapper.process)


                            * [`Mapper.subscribe()`](artifician.processors.mapper.md#artifician.processors.mapper.Mapper.subscribe)


                    * [artifician.processors.normalizer module](artifician.processors.normalizer.md)


                        * [`KeyValuesNormalizer`](artifician.processors.normalizer.md#artifician.processors.normalizer.KeyValuesNormalizer)


                            * [`KeyValuesNormalizer.normalize()`](artifician.processors.normalizer.md#artifician.processors.normalizer.KeyValuesNormalizer.normalize)


                            * [`KeyValuesNormalizer.normalize_key_values()`](artifician.processors.normalizer.md#artifician.processors.normalizer.KeyValuesNormalizer.normalize_key_values)


                        * [`Normalizer`](artifician.processors.normalizer.md#artifician.processors.normalizer.Normalizer)


                            * [`Normalizer.process()`](artifician.processors.normalizer.md#artifician.processors.normalizer.Normalizer.process)


                            * [`Normalizer.subscribe()`](artifician.processors.normalizer.md#artifician.processors.normalizer.Normalizer.subscribe)


                        * [`NormalizerStrategy`](artifician.processors.normalizer.md#artifician.processors.normalizer.NormalizerStrategy)


                            * [`NormalizerStrategy.normalize()`](artifician.processors.normalizer.md#artifician.processors.normalizer.NormalizerStrategy.normalize)


                        * [`PathsNormalizer`](artifician.processors.normalizer.md#artifician.processors.normalizer.PathsNormalizer)


                            * [`PathsNormalizer.get_path_values()`](artifician.processors.normalizer.md#artifician.processors.normalizer.PathsNormalizer.get_path_values)


                            * [`PathsNormalizer.normalize()`](artifician.processors.normalizer.md#artifician.processors.normalizer.PathsNormalizer.normalize)


                        * [`PropertiesNormalizer`](artifician.processors.normalizer.md#artifician.processors.normalizer.PropertiesNormalizer)


                            * [`PropertiesNormalizer.normalize()`](artifician.processors.normalizer.md#artifician.processors.normalizer.PropertiesNormalizer.normalize)


                    * [artifician.processors.processor module](artifician.processors.processor.md)


                        * [`Processor`](artifician.processors.processor.md#artifician.processors.processor.Processor)


                            * [`Processor.process()`](artifician.processors.processor.md#artifician.processors.processor.Processor.process)


                            * [`Processor.subscribe()`](artifician.processors.processor.md#artifician.processors.processor.Processor.subscribe)


        * [Submodules](API.md#submodules)


            * [artifician.dataset module](artifician.dataset.md)


                * [`Dataset`](artifician.dataset.md#artifician.dataset.Dataset)


                    * [`Dataset.add_samples()`](artifician.dataset.md#artifician.dataset.Dataset.add_samples)


                    * [`Dataset.observe()`](artifician.dataset.md#artifician.dataset.Dataset.observe)


                    * [`Dataset.post_process()`](artifician.dataset.md#artifician.dataset.Dataset.post_process)


            * [artifician.feature_definition module](artifician.feature_definition.md)


                * [`FeatureDefinition`](artifician.feature_definition.md#artifician.feature_definition.FeatureDefinition)


                    * [`FeatureDefinition.map()`](artifician.feature_definition.md#artifician.feature_definition.FeatureDefinition.map)


                    * [`FeatureDefinition.observe()`](artifician.feature_definition.md#artifician.feature_definition.FeatureDefinition.observe)


                    * [`FeatureDefinition.process()`](artifician.feature_definition.md#artifician.feature_definition.FeatureDefinition.process)


                    * [`FeatureDefinition.subscribe()`](artifician.feature_definition.md#artifician.feature_definition.FeatureDefinition.subscribe)
