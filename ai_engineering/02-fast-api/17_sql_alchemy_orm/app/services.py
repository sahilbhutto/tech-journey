from models import User, Post
from db import SessionLocal
from sqlalchemy import select


# Create a new user
def create_user(name: str, email: str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


# Get user by ID
def get_user_by_id(user_id: int):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        return user


# Get all users
def get_all_users():
    with SessionLocal() as session:
        statement = select(User)
        users = session.scalars(statement).all()
        return users


# update user by ID
def update_user(user_id: int, name: str = None, email: str = None):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        if name:
            user.name = name
        if email:
            user.email = email
        session.commit()
        session.refresh(user)
        return user

# delete user by ID
def delete_user(user_id: int):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        session.delete(user)
        session.commit()
        return user


# get users ordered by name
def get_users_ordered_by_name():
    with SessionLocal() as session:
        statement = select(User).order_by(User.name)
        users = session.scalars(statement).all()
        return users


# create a new post
def create_post(title: str, content: str, user_id: int):
    with SessionLocal() as session:
        post = Post(title=title, content=content, user_id=user_id)
        session.add(post)
        session.commit()
        session.refresh(post)
        return post


# Get post by ID
def get_post_by_id(post_id: int):
    with SessionLocal() as session:
        statement = select(Post).where(Post.id == post_id)
        post = session.scalars(statement).one()
        return post


# Get all posts
def get_all_posts():
    with SessionLocal() as session:
        statement = select(Post)
        posts = session.scalars(statement).all()
        return posts


# get posts by user ID
def get_posts_by_user_id(user_id: int):
    with SessionLocal() as session:
        statement = select(Post).where(Post.user_id == user_id)
        posts = session.scalars(statement).all()
        return posts


# update post by ID
def update_post(post_id: int, title: str = None, content: str = None):
    with SessionLocal() as session:
        post = session.get_one(Post, post_id)
        if title:
            post.title = title
        if content:
            post.content = content
        session.commit()
        session.refresh(post)
        return post

# delete post by ID
def delete_post(post_id: int):
    with SessionLocal() as session:
        post = session.get_one(Post, post_id)
        session.delete(post)
        session.commit()
        return post

# get posts ordered by title
def get_posts_ordered_by_title():
    with SessionLocal() as session:
        statement = select(Post).order_by(Post.title)
        posts = session.scalars(statement).all()
        return posts
