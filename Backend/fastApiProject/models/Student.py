from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..dbConfig.db import Base


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    address_id = Column(Integer, ForeignKey('Address.address_id'), nullable=True)
    city = Column(String(100), nullable=True)

    address = relationship("Address", back_populates="Students")
