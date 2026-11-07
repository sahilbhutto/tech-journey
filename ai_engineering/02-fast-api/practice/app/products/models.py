from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base
from sqlalchemy import String, Integer, Float


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    desc: Mapped[str] = mapped_column(String(400), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False)
