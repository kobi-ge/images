from pathlib import Path

class IngestionConfig:
    def __init__(self):
        self.host = "kafka"
        self.port = 9092
        self.directory = Path(__file__).resolve().parent / "data"
        

    def get_host(self):
        return self.host
    
    def get_port(self):
        return self.port
