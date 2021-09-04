from pydantic import BaseModel

class Message(BaseModel):
    id: int
    text:dict

class Status(BaseModel):
    message: str
    