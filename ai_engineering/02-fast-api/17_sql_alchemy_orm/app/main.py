from models import create_tables
from services import *

create_tables()


# ===== create a new user ======
# create_user("john_doe", "john@example.com")
# create_user("alice", "alice@example.com")
# create_user("bob", "bob@example.com")
# create_user("charlie", "charlie@example.com")

# ===== get user by ID ======
# user_1 = get_user_by_id(1)
# user_2 = get_user_by_id(2)
# print(f"User 1: {user_1.name}, Email: {user_1.email}")
# print(f"User 2: {user_2.name}, Email: {user_2.email}")

# ===== get all users ======
# all_users = get_all_users()
# print("All Users:", [f"{user.name} ({user.email})" for user in all_users])

# ==== update user by ID ======
# updated_user = update_user(1, name="john_updated", email="john.updated@example.com")

# ===== delete user by ID ======
# deleted_user = delete_user(2)

# ==== get users ordered by name ======
# ordered_users = get_users_ordered_by_name()
# print("Users Ordered by Name:", [f"{user.name} ({user.email})" for user in ordered_users])



# ===== create a new post ======
# create_post("First Post", "This is the content of the first post.", 1)
# create_post("Second Post", "This is the content of the second post.", 1)
# create_post("Third Post", "This is the content of the third post.", 2)
# create_post("Fourth Post", "This is the content of the fourth post.", 3)
# create_post("Fifth Post", "This is the content of the fifth post.", 4)

# ===== get post by ID ======
# post_1 = get_post_by_id(1)
# post_2 = get_post_by_id(2)
# print(f"Post 1: {post_1.title}, Content: {post_1.content}")
# print(f"Post 2: {post_2.title}, Content: {post_2.content}")

# ===== get all posts ======
# all_posts = get_all_posts()
# print("All Posts:", [f"{post.title} (User ID: {post.user_id})" for post in all_posts])

# ===== get posts by user ID ======
# user_1_posts = get_posts_by_user_id(1)
# print("User 1 Posts:", [f"{post.title} (Content: {post.content})" for post in user_1_posts])

# ==== update post by ID ======
# updated_post = update_post(1, title="Updated First Post", content="This is the updated content of the first post.")
# print(f"Updated Post 1: {updated_post.title}, Content: {updated_post.content}")

# ===== delete post by ID ======
# deleted_post = delete_post(2)

# ===== get posts ordered by title ======
# ordered_posts = get_posts_ordered_by_title()
# print("Posts Ordered by Title:", [f"{post.title} (User ID: {post.user_id})" for post in ordered_posts])
