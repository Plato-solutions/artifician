"""
   Copyright 2023 Plato Solutions, Inc.

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
class chain:
    """Manages a chain of processors.

    This class handles the sequential execution of a chain of processors and
    can subscribe to a publisher to trigger the processing.

    Attributes:
        processors (list): A list of processors in the chain.
    """
    def __init__(self, processors=None) -> None:
        """Initializes the chain with an optional list of processors.

        Args:
            processors (list, optional): An initial list of processors to be managed.
        """
        self.processors = processors or []

    def then(self, next_processor) -> 'chain':
        """Adds a processor to the end of the chain.

        Args:
            processor (Processor): The processor to add to the chain.

        Returns:
            processor_chaining (chain): The chain instance.
        """
        if not isinstance(next_processor, list):
            next_processor = [next_processor]

        for processor in next_processor:
            if not hasattr(processor, 'process'):
                raise TypeError("Each processor must have a 'process' method")
            self.processors.append(processor)

        return self

    def process(self, publisher, data: any) -> any:
        """Processes data sequentially through the chain of processors.

        Args:
            data: The data to be processed by the chain.

        Returns:
            The final processed data after passing through all processors.
        """
        if not self.processors:
            raise RuntimeError("Processor chain is empty. Add processors before processing.")
        processed_data = data
        
        for processor in self.processors:
            try:
                processed_data = processor.process(publisher, processed_data)
            except Exception as e:
                raise RuntimeError(f"Error processing data in {processor}: {e}")
        
        publisher.value = processed_data

        return processed_data

    def subscribe(self, publisher, pool_scheduler=None) -> None:
        """Subscribes the processor chain to a feature definition.

        The feature definition will trigger the processing of the chain.

        Args:
            feature_definition (publisher): The feature definition to subscribe to.
        """
        observable = publisher.observe(publisher.EVENT_PROCESSED)
        observable.subscribe(lambda feature_raw: self.process(publisher, feature_raw),
                             scheduler=pool_scheduler)