from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Relationship
from sqlalchemy import String, ForeignKey
from db import engine

class Base(DeclarativeBase):
    pass


# User Model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)

    # one to many relationship with Post model
    posts: Mapped[list["Post"]] = Relationship("Post", back_populates="user", cascade="all, delete")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"


# Post Model
class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    user: Mapped["User"] = Relationship("User", back_populates="posts")


    def __repr__(self) -> str:
        return f"Post(id={self.id}, title={self.title}, content={self.content}, user_id={self.user_id})"


def create_tables():
    Base.metadata.create_all(bind=engine)

def drop_tables():
    Base.metadata.drop_all(bind=engine)
