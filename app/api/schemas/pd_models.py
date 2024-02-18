from datetime import datetime, timedelta
from pydantic import BaseModel

class User(BaseModel):
    id: int
    login: str
    pass_hash: str
    
  
class Token(BaseModel):
    id: str
    token: str
    created: datetime
    live_time: timedelta
    activated: bool
    owner_id: int