from models import User
from db import async_session
from sqlalchemy import select


# Create a new user
async def create_user(name: str, email: str, password: str) -> User:
    async with async_session() as session:
        new_user = User(
            name=name,
            email=email,
            password=password
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user


# Get all users
async def get_all_users() -> list[User]:
    async with async_session() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()

        return list(users)


# Get a user by ID
async def get_user(user_id: int) -> User | None:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()
        return user


# Update a user by ID
async def update_user(
    user_id: int,
    name: str | None = None,
    email: str | None = None,
    password: str | None = None
) -> User | None:

    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()

        if user is None:
            return None

        if name is not None:
            user.name = name

        if email is not None:
            user.email = email

        if password is not None:
            user.password = password

        await session.commit()
        await session.refresh(user)

        return user


# Delete a user by ID
async def delete_user(user_id: int) -> bool:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )

        user = result.scalar_one_or_none()

        if user is None:
            return False

        await session.delete(user)
        await session.commit()

        return True
