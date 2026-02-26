from fastapi import APIRouter
import logging

from orchestrator import IngestionOrchestrator
from config import IngestionConfig
from text_extractor import OCREngine
from metadata import MetadataExtractor
from kafka_producer import KafkaProducer
from mongoloader import MongoLoaderClient

logging.basicConfig(level=logging.DEBUG, format= "%(asctime)s - %(name)-15s - %(levelname)s - %(message)s")
router = APIRouter()
config = IngestionConfig()
OCREngine = OCREngine(logger=logging.getLogger(OCREngine.__module__))
MetadataExtractor = MetadataExtractor(logger=logging.getLogger(MetadataExtractor.__module__))
mongoloader = MongoLoaderClient(url="http://mongodbloader:8001/save_image/", logger=logging.getLogger(MongoLoaderClient.__module__))
producer = KafkaProducer(host=config.host, port=config.port, topic_name="RAW", logger=logging.getLogger(KafkaProducer.__module__))
orchestrator = IngestionOrchestrator(config=config, OCREngine=OCREngine, MetadataExtractor=MetadataExtractor, mongoloader=mongoloader, producer=producer, logger= logging.getLogger(IngestionOrchestrator.__module__))

@router.post("/start")
def start_program():
    orchestrator.run()
    return {"status": "success"}

@router.get("/healthcheck")
def health():
    return {"status": "healthy"} 