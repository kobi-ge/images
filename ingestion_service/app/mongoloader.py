import requests
from requests import ConnectionError

class MongoLoaderClient:
    def __init__(self, url, logger):
        self.client_url = url
        self.logger = logger

    def send_to_mongo_loader(self, data):
        try:
            response = requests.post(url=self.client_url, data=data)
            self.logger.info("image sent to mongoloader")
            return response
        except ConnectionError as e:
            self.logger.error(f"connection error: {e}")