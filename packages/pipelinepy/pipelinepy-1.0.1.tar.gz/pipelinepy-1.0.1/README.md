# pipelinepy

This is a Python client callback for the Pipeline Kafka. It is designed to provide a simple and straightforward interface for interacting with IMS Kafka.

## Installation

To install the pipelinepy, you can use pip (artifactory-uw2 credentials are needed):

```bash
pip install pipelinepy
```

## Usage

To use the pipelinepy, you need to import it in your Python script, along with the kafka client implementation. 
You can then create a Kafka producer and consumer, and use them to send and receive messages to/ from a Kafka topic.

```python
#!/usr/bin/env python
import threading, time

from kafka import KafkaConsumer, KafkaProducer
from pipelinepy import ImsTokenProvider


class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        producer = KafkaProducer(bootstrap_servers=['kafka-a1-az1-va7-corp.int.pipeline.adobedc.net:443','kafka-a1-az2-va7-corp.int.pipeline.adobedc.net:443','kafka-a1-az3-va7-corp.int.pipeline.adobedc.net:443'],
                                 sasl_mechanism='OAUTHBEARER',
                                 security_protocol='SASL_SSL',
                                 sasl_oauth_token_provider=ImsTokenProvider())

        while not self.stop_event.is_set():
            producer.send('xdm_acp_dcs_stg_gw23', b"Hello, world!")
            producer.send('xdm_acp_dcs_stg_gw23', b"Salutare, lume!")
            producer.send('xdm_acp_dcs_stg_gw23', b"\xc2\xa1Hola, mundo!")
            time.sleep(1)

        producer.close()


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=['kafka-a1-az1-va7-corp.int.pipeline.adobedc.net:443','kafka-a1-az2-va7-corp.int.pipeline.adobedc.net:443','kafka-a1-az3-va7-corp.int.pipeline.adobedc.net:443'],
                                 auto_offset_reset='earliest',
                                 group_id='petrut-test-cg',
                                 consumer_timeout_ms=1000,
                                 sasl_mechanism='OAUTHBEARER',
                                 security_protocol='SASL_SSL',
                                 sasl_oauth_token_provider=ImsTokenProvider())
        consumer.subscribe(['xdm_acp_dcs_stg_gw23'])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():

    tasks = [
        Producer(),
        Consumer()
    ]

    # Start threads of a publisher/producer and a subscriber/consumer to 'my-topic' Kafka topic
    for t in tasks:
        t.start()

    time.sleep(30)

    # Stop threads
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()


if __name__ == "__main__":
    main()

```

## Environment Variables

The following environment variables need to be set:

- `IMS_URL`: The URL of the IMS service.
- `IMS_CLIENT_ID`: The client ID for the IMS service.
- `IMS_CLIENT_SECRET`: The client secret for the IMS service.
- `IMS_CLIENT_CODE`: The client code for the IMS service.

## Contributing

Contributions are welcome. Please submit a pull request or create an issue to discuss the changes you want to make.
