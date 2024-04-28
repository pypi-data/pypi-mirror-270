from pydantic import BaseModel
class Message(BaseModel):
    id: int
    sender: str
    recipient: str
    content: str