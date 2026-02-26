class MonogLoaderOrchestrator:
    def __init__(self, config, mongo_service, logger):
        self.config = config
        self.mongo_service = mongo_service
        self.logger = logger

    def run(self, data):
        self.mongo_service.put(data)
        