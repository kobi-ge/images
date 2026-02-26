from PIL import Image, UnidentifiedImageError
import uuid
import os



class MetadataExtractor:
    def __init__(self, logger):
        self.logger = self.logger = logger

    def generate_image_id(self):
        self.image_id = str(uuid.uuid4())
        return self.image_id
    
    def get_metadata(self, image_path: str) -> dict:
        try:
            self.image = Image.open(image_path)
            self.width, self.length = self.image.size
            self.image_format = self.image.format
            self.bytes_size = os.path.getsize(image_path)
            return {
                "image_format": self.image_format,
                "width": self.width,
                "length": self.length,
                "bytes_size": self.bytes_size
            }
        except UnidentifiedImageError as e:
            self.logger.error(f"error: {e}")

    def get_image_bytes(self, image_path: str) -> bytes:
        with open(image_path, "rb") as file:
            return file.read()
