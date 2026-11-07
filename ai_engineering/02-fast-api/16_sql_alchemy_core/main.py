from tables import create_tables
from services import *


# CREATE DATABASE TABLES
create_tables()
print("Database tables created successfully!")

# CREATE USERS
print("\n--- Creating Users ---")
user1_id = create_user(
    "Sahil Ali",
    "sahil.dev@gmail.com",
    "dummy_hash_1",
)

user2_id = create_user(
    "Ali Abbass",
    "ali.dev@gmail.com",
    "dummy_hash_2",
)

print(f"User 1 created with ID: {user1_id}")
print(f"User 2 created with ID: {user2_id}")


# GET SINGLE USER
print("\n--- Get Single User ---")

user = get_user_by_id(user1_id)
print(f"User fetched: {user}")


# GET ALL USERS
print("\n--- Get All Users ---")

all_users = get_all_users()

for user in all_users:
    print(user)


# UPDATE USER NAME
print("\n--- Update User ---")

updated = update_user_name(user1_id, "Sahil Ali Bhutto")
print(f"User updated: {updated}")

print(f"Updated user: {get_user_by_id(user1_id)}")


# CREATE POSTS
print("\n--- Creating Posts ---")

post1_id = create_post(
    user1_id,
    "ReactJS",
    "A new era of frontend development with React.js.",
)

post2_id = create_post(
    user2_id,
    "Frontend Development in 2026",
    "AI is changing web development, but frontend engineering remains important.",
)

print(f"Post 1 created with ID: {post1_id}")
print(f"Post 2 created with ID: {post2_id}")


# GET SINGLE POST
print("\n--- Get Single Post ---")

post = get_post_by_id(post1_id)
print(f"Post fetched: {post}")


# GET ALL POSTS
print("\n--- Get All Posts ---")

all_posts = get_all_posts()

for post in all_posts:
    print(post)


# GET POSTS BY USER ID
print("\n--- Get Posts By User ---")

user_posts = get_posts_by_user_id(user1_id)

for post in user_posts:
    print(post)

# UPDATE POST
print("\n--- Update Post ---")

updated = update_post(
    post1_id,
    "React.js in 2026",
    "React.js continues to be an important frontend library.",
)

print(f"Post updated: {updated}")
print(f"Updated post: {get_post_by_id(post1_id)}")

# DELETE POST
print("\n--- Delete Post ---")

deleted = delete_post(post2_id)
print(f"Post deleted: {deleted}")

print(f"Deleted post lookup: {get_post_by_id(post2_id)}")

# DELETE USER
print("\n--- Delete User ---")

deleted = delete_user(user2_id)
print(f"User deleted: {deleted}")


# FINAL DATABASE STATE
print("\n--- Final Users ---")

for user in get_all_users():
    print(user)


print("\n--- Final Posts ---")

for post in get_all_posts():
    print(post)


print("\n--- CRUD Testing Completed ---")
