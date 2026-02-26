from pathlib import Path
import os

class IngestionConfig:
    def __init__(self):
        self.host = os.getenv("KAFKA_SERVICE")
        self.port = int(os.getenv("KAFKA_PORT"))
        self.directory = Path(__file__).resolve().parent / "data"


    def get_host(self):
        return self.host
    
    def get_port(self):
        return self.port
