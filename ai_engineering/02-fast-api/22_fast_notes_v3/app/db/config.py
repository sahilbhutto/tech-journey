from fastapi.params import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import os
from typing import Annotated


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db_path= os.path.join(BASE_DIR, "sqlite.db")

DATABASE_URL = f"sqlite+aiosqlite:///{db_path}"


engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with async_session() as session:
        yield session

SessionDependency = Annotated[AsyncSession, Depends(get_db)]
