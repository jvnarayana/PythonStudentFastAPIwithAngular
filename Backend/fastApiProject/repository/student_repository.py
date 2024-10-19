from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from ..models.Student import Student


async def get_all_students(db: AsyncSession):
    result = await db.execute(select(Student).options(selectinload(Student.address)))
    return result.scalars().all()


async def get_student_by_id(db: AsyncSession, student_id: int) -> Student:
    result = await db.execute(select(Student).where(Student.id == student_id))
    return result.scalar()


async def create_student(db: AsyncSession, student: Student) -> Student:
    db.add(student)
    await db.commit()
    await db.refresh(student)
    return student


async def update_student(db: AsyncSession, student_id: int, updated_data: dict) -> Student:
    student = await get_student_by_id(db, student_id)
    for key, value in updated_data.items():
        setattr(student, key, value)
    await db.commit()
    await db.refresh(student)
    return student


async def delete_student(db: AsyncSession, student_id: int):
    student = await get_student_by_id(db, student_id)
    if student:
        await db.delete(student)
        await db.commit()
    return student
