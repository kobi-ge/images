import os

class MongoLoaderConfig:
    def __init__(self):
        self.host = os.getenv("HOST" ,"localhost")
        self.port = os.getenv("PORT" ,27017)
        self.user = os.getenv("USER" ,"kodi")
        self.password = os.getenv("PASSWORD" ,"word")
        self.uri = f"mongodb://{self.user}:{self.password}@{self.host}:{self.port}"

    