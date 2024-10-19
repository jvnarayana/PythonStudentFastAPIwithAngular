from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..dbConfig.db import Base


class Address(Base):
    __tablename__ = "address"

    address_id = Column(Integer, primary_key=True, index=True)
    street_number = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, nullable=True)
    zipcode = Column(Integer, nullable=True)


 
    students = relationship("Student", back_populates="address")
    teachers = relationship("Teacher", back_populates="address")