import logging

from config import CleaningConfig
from kafka_consumer import KafkaConsumer
from text_cleaner import clearing_the_data, remove_stop_words
from kafka_producer import KafkaProducer
from orchestrator import CleaningOrchestrator

logging.basicConfig(level=logging.DEBUG, format= "%(asctime)s - %(name)-15s - %(levelname)s - %(message)s")

config = CleaningConfig(logger=logging.getLogger(CleaningConfig.__module__))
consumer = KafkaConsumer(
                host=config.host, 
                port=config.port, 
                topic_name="clean", 
                logger=logging.getLogger(KafkaConsumer.__module__))
producer = KafkaProducer(
    host=config.host,
    port=config.port,
    topic_name="Analytic",
    logger=logging.getLogger(KafkaProducer.__module__))
orchestrator = CleaningOrchestrator(
    config=config,
    consumer=consumer,
    punct_callback=clearing_the_data(),
    words_callback=remove_stop_words(),
    producer=producer,
    logger=logging.getLogger(CleaningOrchestrator.__module__)
)

orchestrator.run()