import logging
from fastapi import FastAPI, Request

from config import MongoLoaderConfig
from storage import MongoService
from orchestrator import MonogLoaderOrchestrator

logging.basicConfig(level=logging.DEBUG, format= "%(asctime)s - %(name)-15s - %(levelname)s - %(message)s")

config = MongoLoaderConfig()
mongo_service = MongoService(uri=config.uri, logger=logging.getLogger(MongoService.__module__))
mongo_service.connect()
mongo_service.create_fs()
orchestrator = MonogLoaderOrchestrator(config=config, mongo_service=mongo_service, logger=logging.getLogger(MonogLoaderOrchestrator.__module__))

app = FastAPI()

@app.post("/save_image")
async def save_image(request: Request):
    image = await request.body()
    orchestrator.run()
