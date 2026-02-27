import json

from confluent_kafka import Consumer

class KafkaConsumer:
    def __init__(self, host, port, topic_name, logger):
        self.host = host
        self.port = port
        self.consumer_config = {
            "bootstrap.servers": f"{self.host}:{self.port}",
            "group.id": "team-clean",
            "auto.offset.reset": "earliest"
        }
        self.consumer = Consumer(self.consumer_config)
        self.consumer.subscribe([topic_name])
        self.logger = logger
        self.logger.info(f"🟢 Consumer is running and subscribed to {topic_name} topic")

    def consume(self):
        try:
            msg = self.consumer.poll(1.0)
            if msg is None:
                return None
            if msg.error():
                self.logger.error("❌ Error:", msg.error())
                return None

            value = msg.value().decode("utf-8")
            value = json.loads(value)
            self.logger.error(f"recieved image: {value}")
            return value
        except KeyboardInterrupt:
            self.logger.info("\n🔴 Stopping consumer")

    def close_consumer(self):
        return self.consumer.close()
