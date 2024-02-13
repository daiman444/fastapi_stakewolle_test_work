from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    password: int
    age: int
    
    
class Feedback(BaseModel):
    name: str
    message: str