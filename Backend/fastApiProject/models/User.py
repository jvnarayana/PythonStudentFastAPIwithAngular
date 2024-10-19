from typing import Any

from sqlalchemy import Column, Integer, String
from ..dbConfig.db import Base


class User(Base):
    def __init__(self, **kw: Any):
        super().__init__(kw)
        self.password = None

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(150), nullable=True)
    password_hash = Column(String(255), nullable=True)
