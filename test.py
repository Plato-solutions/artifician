
from artifician import *
from artifician.processors.text_processors.tokenizer import TokenizationProcessor
from artifician.processors.text_processors.stemlemtizer import StemLemProcessor
from artifician.processors.text_processors.stop_word_remover import StopWordsRemoverProcessor
from artifician.processors.text_processors.text_cleaner import TextCleaningProcessor

cleaner = TextCleaningProcessor(lowercase=True, remove_punctuation=True, remove_numbers=True, strip_whitespace=True, remove_html_tags=True, remove_urls=True)
tokenizer = TokenizationProcessor(method='word')
stemlem = StemLemProcessor()
stopword = StopWordsRemoverProcessor()
mapper = Mapper(FeatureMap({"":0}))

def get_text(text):
    return text

sample_texts = [
        "The quick brown fox jumps over the lazy dog!",
        "<p>The HTML tags should be removed.</p>",
]
dataset = Dataset()
feature = FeatureDefinition(get_text, [dataset])
clean_text_pipeline = cleaner.then(tokenizer).then(stemlem).then(stopword).then(mapper)
clean_text_pipeline.subscribe(feature)
datastore = dataset.add_samples(sample_texts)
print(datastore)
# dataset = Dataset()
# feature = FeatureDefinition(get_node_attribute, [dataset],  "class")

# tokenizer = TokenizationProcessor(method='word')
# text_normalizer = Normalizer(PropertiesNormalizer(), delimiter = {'delimiter': [" "]})


# # chain = text_normalizer.then(mapper).then(add_processor)
# chain = ProcessorChainManager([text_normalizer, mapper, add_processor])

# # processor_chain = ProcessorChainManager([text_normalizer , mapper])
# chain.subscribe(feature)
# datastore = dataset.add_samples(list(html_elements))
# print(datastore)




# class add_two(processor.Processor):
#     def __init__(self):
#         super().__init__()

#     def process(self, publisher, data):
#         publisher.value = data * 2 
#         return data * 2
    
#     def subscribe(self, publisher, pool_scheduler=None):
#         """Defines logic for subscribing to an event in publisher

#         Args:
#             publisher (object): instance of publisher

#             pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

#         Return:
#             None
#         """

#         observable = publisher.observe(publisher.EVENT_PROCESSED)
#         observable.subscribe(lambda feature_raw: self.process(publisher, feature_raw),
#                              scheduler=pool_scheduler)