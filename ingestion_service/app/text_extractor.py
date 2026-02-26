import pytesseract
from pytesseract import TesseractError
from PIL import Image




class OCREngine:
    def __init__(self, logger):
        self.logger = logger

    def extract_text(self, path):
        try:
            self.image = Image.open(path)
            self.extracted_text = pytesseract.image_to_string(self.image)
            return self.extracted_text
        except TesseractError as e:
            self.logger.error(f"error: {e}")
        except Exception as e:
            self.logger.error(f"error: {e}")
    

