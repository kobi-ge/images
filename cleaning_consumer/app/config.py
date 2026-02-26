import os

class CleaningConfig:
    def __init__(self, logger):
        self.host = os.getenv("KAFKA_SERVICE")
        self.port = int(os.getenv("KAFKA_PORT"))
        self.logger = logger