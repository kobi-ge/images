import requests

class MongoLoaderClient:
    def __init__(self, url, logger):
        self.client_url = url
        self.logger = logger

    def send_to_mongo_loader(self, data):
        response = requests.post(url=self.client_url, data=data)
        return response
