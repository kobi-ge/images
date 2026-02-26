class CleaningOrchestrator:
    def __init__(self, config, consumer, punct_callback, words_callback, producer, logger):
        self.config = config
        self.consumer = consumer
        self.punct_callback = punct_callback
        self.words_callback = words_callback
        self.producer = producer
        self.logger = logger

    def run(self):
        while True:
            try:
                image_info = self.consumer.consume()
                image_info = self.punct_callback(image_info)
                image_info = self.words_callback(image_info)
                self.producer.produce(image_info)
                self.logger.info(f"image: {image_info} successfully sent to kafka")
            except Exception as e:
                self.logger.error(f"error: {e}")
