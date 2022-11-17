import multiprocessing
import unittest
from rx.scheduler import ThreadPoolScheduler
import os
from urllib.parse import urlparse
from artifician.dataset import Dataset
from artifician.feature_definition import FeatureDefinition
from artifician.processors.normalizer import Normalizer, PropertiesNormalizer, PathsNormalizer


def extract_filename(url):
    """extract the filename of the url

    Args:
        url(string): url

    Return:
        filename(string): filename of the url

    """

    filename = os.path.basename(urlparse(url).path)

    if filename.endswith('.html'):
        return filename
    else:
        return ''


def extract_path(url, delimiter, path_joiner):
    """extract the path of the url

    Args:
        url(string): url
        delimiter(string): delimiter to split the path
        path_joiner(string): path joiner to join the path

    Return:
        url_path(string): path of the url

    """
    url_path = urlparse(url).path

    if url_path.endswith('html'):
        url_path = path_joiner.join(url_path.split(delimiter)[:-1])

    return url_path


class test_FeatureDefinition(unittest.TestCase):

    def test_process(self):
        optimal_thread_count = multiprocessing.cpu_count()
        pool_scheduler = ThreadPoolScheduler(optimal_thread_count)
        url = ['https://mirasvit.com/knowledge-base/tips-on-how-to-change-the-magento-base-url-in-default-magento.html']
        expected_output = [[('knowledge-base/', 0)],
                           [('tips', 0), ('on', 1), ('how', 2), ('to', 3), ('change', 4), ('the', 5), ('magento', 6),
                            ('base', 7), ('url', 8), ('in', 9), ('default', 10), ('magento.html', 11)]]
        dataset = Dataset()

        url_filename = FeatureDefinition(extract_filename)
        url_path = FeatureDefinition(extract_path, "/", "/")
        properties_normalizer = Normalizer(PropertiesNormalizer(), delimiter={'delimiter': ["--"]})
        paths_normalizer = Normalizer(PathsNormalizer(), delimiter={'delimiter': ["/"]})

        properties_normalizer.subscribe(url_filename, pool_scheduler)
        paths_normalizer.subscribe(url_path, pool_scheduler)
        url_path.subscribe(dataset, pool_scheduler)
        url_filename.subscribe(dataset, pool_scheduler)

        dataset.add_samples(url)
        for i in dataset.datastore.values:
            print(i)
        print(dataset.datastore.loc[0, 1:].to_list())
        self.assertEqual(dataset.datastore.loc[0, 1:].to_list(), expected_output)
