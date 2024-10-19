from pydantic import BaseModel
from typing import List, Optional


class StudentBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    city: Optional[str]


class StudentCreate(StudentBase):
    address_id: Optional[int]


class Student(StudentCreate):
    id: int
    address_id: Optional[int]

    class Config:
        orm_mode = True
