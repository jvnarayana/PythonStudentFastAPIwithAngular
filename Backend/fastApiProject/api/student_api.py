from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..dbConfig.db import get_db
from ..models.Student import Student
from ..repository.student_repository import get_all_students, get_student_by_id, create_student, update_student, \
    delete_student
from ..services.cache_service import get_cache, set_cache

router = APIRouter()


@router.get("/students", response_model=List[Student])
async def get_students(db: AsyncSession = Depends(get_db)):
    students = await get_all_students(db)

    if not students:
        return HTTPException(status_code=404, detail="No students found")
    return students


@router.get("/students/{student_id}", response_model=Student)
async def get_studentById(student_id: int, db: AsyncSession = Depends(get_db)):
    cache_key = f"student_{student_id}"
    cached_student = await get_cache(cache_key)
    if cached_student:
        return cached_student
    student = await get_student_by_id(db, student_id)
    await set_cache(cache_key, student)
    return student


@router.post("/student", response_model=Student)
async def create_students(student: Student, db: AsyncSession = Depends(get_db)):
    return await create_student(db, student)


@router.put("/student/{student_id}", response_model=Student)
async def update_students(student_id: int, student: Student, db: AsyncSession = Depends(get_db)):
    return await update_student(db, student_id, student)


@router.delete("/student/{student_id}", response_model=Student)
async def delete_students(student_id: int, db: AsyncSession = Depends(get_db)):
    return await delete_student(id, student_id)
