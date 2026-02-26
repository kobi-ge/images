import os


class IngestionOrchestrator:
    def __init__(self, config, OCREngine, MetadataExtractor, mongoloader, producer, logger):
        self.config = config
        self.OCREngine = OCREngine
        self.MetadataExtractor = MetadataExtractor
        self.mongoloader = mongoloader
        self.producer = producer
        self.logger = logger
        
    def process_image(self, image_path):
        self.metadata = self.MetadataExtractor.get_metadata(f"{self.config.directory}/{image_path}")
        self.image_id = self.MetadataExtractor.generate_image_id()
        self.image_bytes = self.MetadataExtractor.get_image_bytes(f"{self.config.directory}/{image_path}")
        self.metadata['image_id'] = self.image_id
        self.text = self.OCREngine.extract_text(f"{self.config.directory}/{image_path}")
        self.image_info = {
            "text": self.text,
            "metadata": self.metadata
        }
        self.logger.info(f"image info was created: {self.image_info}")
        self.mongoloader.send_to_mongo_loader({self.image_id: self.image_bytes})
        self.logger.info(f"image bytes was created")
        self.producer.produce(self.image_info)

    def run(self):
        for image_path in os.listdir(self.config.directory):
            self.logger.info(f"image path: {image_path}")
            if image_path.endswith(".png"):
                self.process_image(image_path)

