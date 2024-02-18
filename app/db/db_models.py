from typing import List
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.sqltypes import (
    String, Integer, Text,
    DateTime, Boolean
)

from api.schemas.settings import settings


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(
        primary_key=True,
        type_=Integer,
        unique=True,
        index=True,
        autoincrement=True,
    )
    login: Mapped[str] = mapped_column(
        type_=String(32),
        nullable=False,
        unique=True,
    )
    email: Mapped[str] = mapped_column(
        type_=String(32),
        nullable=False,
        unique=True,
    )
    pass_hash: Mapped[str] = mapped_column(
        type_=Text,
        nullable=False,
        unique=True,
    )
    tokens: Mapped[List["Token"]] = relationship(
        back_populates="owner",
    )

    def set_pass_hash(self, password: str):
        self.pass_hash = generate_password_hash(password=password)
        
    def get_pass(self, password: str):
        return check_password_hash(self.pass_hash, password=password)
    
    
class Token(Base):
    __tablename__ = "token"
    
    id: Mapped[int] = mapped_column(
        type_=Integer,
        primary_key=True,
        unique=True,
        index=True,
        autoincrement=True,
    )
    token: Mapped[str] = mapped_column(
        type_=Text,
        unique=True,
        nullable=False,
    )
    created: Mapped[datetime.utcnow] = mapped_column(
        type_=DateTime,
        default=datetime.utcnow,
    )
    live_time: Mapped[int] = mapped_column(
        type_=Integer,
        default=timedelta(
            seconds=settings.TOKEN_LIFE_TIME,
        )
    )
    activated: Mapped[bool] = mapped_column(
        type_=Boolean,
        unique=False,
        default=False,
    )
    owner_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        type_=Integer,
        nullable=False,
    )    
    owner: Mapped["Users"] = relationship(
        back_populates="tokens",
    )

    def token_is_alive(self):
        time_delda: timedelta = datetime.utcnow() - self.created
        return self.live_time > time_delda.total_seconds()
    
    