from confluent_kafka import Producer, KafkaError

import json



class KafkaProducer:
    def __init__(self, host, port, topic_name, logger):
        self.topic_name = topic_name
        self.host = host
        self.port = port
        self.producer = Producer({"bootstrap.servers": f"{self.host}:{self.port}"})
        self.logger = logger

    def delivery_report(self, err, msg):
        if err:
            print(f"❌ Delivery failed: {err}")
        else:
            print(f"✅ Delivered {msg.value().decode('utf-8')}")
            print(f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}")

    def produce(self, value):
        try:
            value = json.dumps(value).encode("utf-8")
            self.producer.produce(
                topic=self.topic_name,
                value=value,
                callback=self.delivery_report
            )
            self.producer.flush()
            self.logger.info(f"message: {value} was sent to kafka")
        except KafkaError as e:
            self.logger.error(f"error: {e}")
