from artifician import *
import pytest

class TestProcessorChainManager:

    # can add processors to the chain using 'then' method
    def test_add_processors_to_chain(self):
        normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': [" "]})
        mapper = Mapper(feature_map=FeatureMap({"": 0}))
        manager = normalizer.then(mapper)

        assert len(manager.processors) == 2
        assert manager.processors[0] == normalizer
        assert manager.processors[1] == mapper

    # can process data sequentially through the chain of processors using 'process' method
    def test_process_data_sequentially(self):
        normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': [" "]})
        mapper = Mapper(feature_map=FeatureMap({"": 0}))
        manager = normalizer.then(mapper)
        data = "data"
        publisher = Dataset()
        result = manager.process(publisher, data)
        
        assert result == [1]


    # raises a TypeError when adding a processor without a 'process' method
    def test_add_processor_without_process_method(self):
        class ProcessorWithoutProcessMethod():
            def __init__(self):
                super().__init__()
        processor = ProcessorWithoutProcessMethod()
        manager = chain()

        with pytest.raises(TypeError):
            manager.then(processor)

    # raises a RuntimeError when processing an empty processor chain
    def test_process_empty_chain(self):
        manager = chain()
        publisher = Dataset()
        data = "data"

        with pytest.raises(RuntimeError):
            manager.process(publisher, data)
