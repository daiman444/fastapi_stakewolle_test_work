from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import (
    Column, Integer, String, 
    ForeignKey, DateTime, Boolean
)
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, 
                primary_key=True, 
                unique=True, 
                index=True, 
                autoincrement=True)
    login = Column(String(32),
                   nullable=False,
                   unique=True)
    email = Column(String(32),
                   nullable=False,
                   unique=True)
    pass_hash = Column(String(16),
                       nullable=False,
                       unique=True)
    tokens = relationship("Token", back_populates="owner")
    
    def set_pass_hash(self, password: str):
        self.pass_hash = generate_password_hash(password=password)
        
    def get_pass(self, password: str):
        return check_password_hash(self.pass_hash, password=password)
    
    
class Token(Base):
    __tablename__ = "token"
    
    id = Column(Integer,
                primary_key=True,
                unique=True,
                index=True,
                autoincrement=True)
    token = Column(String(32),
                   unique=True,
                   nullable=False)
    created = Column(DateTime, 
                     default=datetime.utcnow)
    live_time = Column(Integer,
                       default=timedelta(seconds=900) )
    activated = Column(Boolean, 
                       unique=False,
                       default=False)
    owner_id = Column(Integer, 
                      ForeignKey("users.id",),
                      nullable=False)
    owner = relationship("Users",
                         back_populates="tokens")
    
    def token_is_alive(self):
        time_delda: timedelta = datetime.utcnow() - self.created
        return self.live_time > time_delda.total_seconds()
    
    