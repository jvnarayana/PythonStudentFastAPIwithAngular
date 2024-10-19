from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dbConfig.db import Base
from .Address import Address


class Teacher(Base):
    __tablename__ = 'teacher'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    address_id = Column(Integer, ForeignKey('addresses.address_id'), nullable=True)
    city = Column(String, nullable=True)

    address = relationship("Address", back_populates="teachers")