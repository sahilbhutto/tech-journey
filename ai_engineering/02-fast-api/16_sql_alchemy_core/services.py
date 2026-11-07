from sqlalchemy import insert, select, update, delete
from db import engine
from tables import users, posts


# USERS CRUD

# CREATE: Add a new user
def create_user(name: str, email: str, password: str) -> int:
    with engine.begin() as connection:
        query = insert(users).values(
            name=name,
            email=email,
            password=password,
        )

        result = connection.execute(query)
        return result.inserted_primary_key[0]


# READ: Get a single user by ID
def get_user_by_id(user_id: int):
    with engine.connect() as connection:
        query = select(users).where(users.c.id == user_id)
        result = connection.execute(query).first()

        return result


# READ: Get all users
def get_all_users():
    with engine.connect() as connection:
        query = select(users)
        result = connection.execute(query).fetchall()

        return result


# UPDATE: Update a user's name
def update_user_name(user_id: int, new_name: str) -> bool:
    with engine.begin() as connection:
        query = (
            update(users)
            .where(users.c.id == user_id)
            .values(name=new_name)
        )

        result = connection.execute(query)
        return result.rowcount > 0


# DELETE: Delete a user
def delete_user(user_id: int) -> bool:
    with engine.begin() as connection:
        query = delete(users).where(users.c.id == user_id)

        result = connection.execute(query)
        return result.rowcount > 0


# POSTS CRUD

# CREATE: Add a new post
def create_post(user_id: int, title: str, content: str) -> int:
    with engine.begin() as connection:
        query = insert(posts).values(
            user_id=user_id,
            title=title,
            content=content,
        )

        result = connection.execute(query)
        return result.inserted_primary_key[0]


# READ: Get a single post by ID
def get_post_by_id(post_id: int):
    with engine.connect() as connection:
        query = select(posts).where(posts.c.id == post_id)
        result = connection.execute(query).first()

        return result


# READ: Get all posts
def get_all_posts():
    with engine.connect() as connection:
        query = select(posts)
        result = connection.execute(query).fetchall()

        return result


# READ: Get all posts belonging to a user
def get_posts_by_user_id(user_id: int):
    with engine.connect() as connection:
        query = select(posts).where(posts.c.user_id == user_id)
        result = connection.execute(query).fetchall()

        return result


# UPDATE: Update a post's title and content
def update_post(post_id: int, new_title: str, new_content: str) -> bool:
    with engine.begin() as connection:
        query = (
            update(posts)
            .where(posts.c.id == post_id)
            .values(
                title=new_title,
                content=new_content,
            )
        )

        result = connection.execute(query)
        return result.rowcount > 0


# DELETE: Delete a post
def delete_post(post_id: int) -> bool:
    with engine.begin() as connection:
        query = delete(posts).where(posts.c.id == post_id)

        result = connection.execute(query)
        return result.rowcount > 0

const
