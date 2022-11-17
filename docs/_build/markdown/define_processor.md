# Defining new processor

If the predefined processors in the library does not satisfy your requirement,
in that case you will need to define your own processor. Let’s look at the a simple
example for defining a new processor.

First of all, we need to set up the connection between the publisher and the processor.
Inside the subscribe you should define the logic for the making the connection.

```default
def subscribe(self, publisher, pool_scheduler=None):

    observable = publisher.observe(publisher.EVENT_PROCESSED)
    observable = observable.subscribe(lambda value: self.process(publisher, value), scheduler=pool_scheduler)
```

The observe method tells that processor is listening to the <EVENT_PROCESSED> function/event of the publisher.
Here you must know which event you want processor to listen to and replace EVENT_PROCESSED with the appropriate event name.
After that, we need to call the process method of the processor, this basically means which operation should be performed
when the event occurs inside the publisher. This is done by calling the subscribe method on the
[observable](https://rxpy.readthedocs.io/en/latest/reference_observable_factory.html#reactivex.Observable)  instance.
while calling process method we need to pass the publisher instance along with the parameters that are passed by publisher.
In above example value contains the parameter passed by the publisher. pool_scheduler is used for achieving cpu concurrency.
You need to pass [scheduler](https://rxpy.readthedocs.io/en/latest/reference_scheduler.html) instance.

Now, you just need to define the process method of the processor.

```default
def process(self, publisher, value):

    processed_value = value * 2
    publisher.value = processed_value
```

Inside process method you need to write your own logic for processing the data. One very important thing to note here is you can
not just return the processed data because publisher can have multiple processors listening to it at the same time. So Instead
of returning you should update the appropriate variables inside the publisher instance. please go through the API documentation
of predefined processor to get the better understanding.

Let’s look at the how the final processor would look like.

```default
from . import Processor

class split_string(Processor.processor):

    def process(self, publisher, string):

        string_spllited = string.split(" ")
        publisher.feature_value = string_splitted

    def subscribe(self, publisher, pool_scheduler=None):

        observable = publisher.observe(publisher.EVENT_PROCESSED)
        observable = observable.subscribe(lambda string: self.process(publisher, string), scheduler = pool_scheduler)
```
