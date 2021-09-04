"""
FastAPI
"""

from fastapi import FastAPI, Depends
from PRODUCER.commons.logger import get_logger
from PRODUCER.pydantic.holders import Message, Status
from PRODUCER.connector.ws import WebSocketConnector

logger = get_logger('main.py')
logger.info(Message.schema_json())

async def get_websocket() -> WebSocketConnector:
    return WebSocketConnector()

logger.info('   Initiliazing Fast API app')
app = FastAPI(title="FastAPI")

@app.on_event("shutdown")
async def shutdown_event(websocket:WebSocketConnector = Depends(get_websocket)):
    logger.info('   shutdown_event function is executing')
    websocket.close()
    logger.info('   websocket connection closed')

logger.info('   Initialized Fast API app')


@app.post("/producer", response_model=Status)
async def produce(message:Message, websocket:WebSocketConnector = Depends(get_websocket)):
    logger.info('   produce function is executing')
    logger.info(message.json())
    websocket.send(message.json())
    return Status(message="SUCCESS")

logger.info('   End of the main file')
