from rx.subject import Subject


class FeatureDefinition:
    """Contains all the functionality for preparing single feature

    Attributes:
        value (any): value of the feature
        cached (dictionary): {event: rx.core.observable.observable.Observable}
        extractor (function): extract feature value from the artifician
        EVENT_PROCESSED (function): event that processes the feature
        MAP_VALUES (function): event that maps values of feature
    """

    def __init__(self, extractor=lambda sample: sample):
        self.value = None
        self.cached = {}
        self.extractor = extractor
        self.EVENT_PROCESSED = self.process
        self.MAP_VALUES = self.map

    def process(self, publisher, sample):
        """process the artifician to build feature value
        process should contain all the logic for completely processing the feature value

        Args:
            sample (any): artifician data
            publisher (object): instance of publisher

        Return:
            feature_processed (list): processed feature_raw
        """
        self.value = self.extractor(sample)

        if self.process in self.cached:
            self.cached[self.process].on_next(self.value)

        self.map(self.value)

        publisher.features_sample.append(self.value)

    def map(self, feature_value):
        """Map the feature value from into int or list of int

        Args:
            feature_value (any): feature value that needs to be mapped

        Return:
            None
        """

        if self.map in self.cached:
            self.cached[self.map].on_next(feature_value)

    def observe(self, event):
        """build and return observable for given event

        Args:
            event (function): function to create observable from
        Return:
            observable (rx.core.observable.observable.Observable): Observable
        """

        if event not in self.cached:
            self.cached[event] = Subject()

        return self.cached[event]

    def subscribe(self, publisher, pool_scheduler=None):
        """Defines logic for subscribing to an event in publisher

        Args:
            publisher (object): publisher instance
            pool_scheduler (rx.scheduler.ThreadPoolScheduler): scheduler instance for concurrency

        Return:
            None
        """

        observable = publisher.observe(publisher.PREPARE_DATASET)
        observable.subscribe(lambda feature_raw: self.process(publisher, feature_raw),
                             scheduler=pool_scheduler)
