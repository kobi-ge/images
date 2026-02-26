class CleaningOrchestrator:
    def __init__(self, config, consumer, text_cleaner, producer, logger):
        self.config = config
        self.consumer = consumer
        self.text_cleaner = text_cleaner
        self.producer = producer
        self.logger = logger

    def run(self):
        while True:
            try:
                image_info = self.consumer.consume()
                image_info = self.text_cleaner.clearing_the_data(image_info)
                image_info = self.text_cleaner.remove_stop_words(image_info)
                self.producer.produce(image_info)
                self.logger.info(f"image: {image_info} successfully sent to kafka")
            except Exception as e:
                self.logger.error(f"error: {e}")
