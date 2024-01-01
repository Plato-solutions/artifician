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
import logging
from abc import ABC, abstractmethod
from artifician.processors.chain import chain

class Processor(ABC):
    """
    Interface for processors in the Artifician library, updated for processor chaining.

    This abstract class defines the interface for processors, including methods for processing data
    and subscribing to publishers, along with the ability to chain processors.
    """

    def __init__(self):
        self.next_processor = None
        self.chain_manager = None
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def process(self, publisher, *data):
        """
        Process the data and update the publisher with the processed values.

        Args:
            publisher: The publisher to which the processed data will be updated.
            data: The data to be processed.
        """
        pass

    @abstractmethod
    def subscribe(self, publisher, pool_scheduler=None):
        """
        Subscribe the processor to a publisher (e.g., FeatureDefinition).

        Args:
            publisher: The publisher to subscribe to.
            pool_scheduler (optional): The scheduler to be used for subscription.
        """
        pass

    def then(self, next_processor):
        """
        Link this processor to the next one in the chain.

        Args:
            next_processor: The next processor to add to the chain.

        Returns:
            chain: chain of processors

        Raises:
            TypeError: If the next_processor is not a valid processor instance.
        """
        try:
            # Assuming all processors have a 'process' method
            if not hasattr(next_processor, 'process'):
                raise TypeError("The next_processor must be a valid processor instance")

            if not self.chain_manager:
                self.chain_manager = chain([self])

            self.next_processor = next_processor
            self.chain_manager.then(next_processor)
            return self.chain_manager

        except Exception as e:
            self.logger.exception(f"Error in chaining processor: {e}")
            raise
