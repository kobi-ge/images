from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import gridfs



class MongoService:
    def __init__(self, uri, logger):
        self.client = None
        self.db = None
        self.uri = uri
        self.logger = logger 

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.client.admin.command('ping')
            self.logger.info("connection established")
        except ConnectionFailure as e:
            self.logger.error(f"connection failed: {e}")
        
    def create_fs(self):
        self.db = self.client['images_db']
        self.fs = gridfs.GridFS(self.db)
        return self.fs
        
    def put(self, value):
        try:
            result = self.fs.put(value)
            self.logger.info(result)
            return result
        except Exception as e:
            self.logger.error(f"put operation failed: {e}")
    

