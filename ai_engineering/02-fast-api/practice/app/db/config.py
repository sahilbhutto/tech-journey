from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DB_PATH = os.path.join(BASE_PATH, 'sqlite.db')

DATABASE_URL = f"sqlite+aiosqlite:///${DB_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
