from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
from db import engine

metadata = MetaData()

users = Table(
  "users",
  metadata,
  Column("id", Integer, nullable=False, primary_key=True),
  Column("name", String(length=30), nullable=False),
  Column("email", String, nullable=False),
  Column("password", String, nullable=False)
)

posts = Table(
  "posts",
  metadata,
  Column("id", Integer, nullable=False, primary_key=True),
  Column("title", String(length=30), nullable=False),
  Column("content", String(length=200), nullable=False),
  Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
)

def create_tables():
  metadata.create_all(engine)
