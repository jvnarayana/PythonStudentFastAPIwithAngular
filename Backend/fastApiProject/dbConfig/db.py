from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URL, future=True, echo=True)
AsyncSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

Base = declarative_base()
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        await session.close()
        await engine.dispose()
        await AsyncSessionLocal.async_close()
