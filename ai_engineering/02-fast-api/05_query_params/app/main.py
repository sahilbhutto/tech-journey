from fastapi import FastAPI

app = FastAPI()

# Single Query Parameter
@app.get("/products")
async def get_products(category: str):
  return {
    "status": "ok",
    "category": category
  }

# Multiple Query Parameter
@app.get("/books")
async def get_books(type: str, page: int, limit: int):
  return {
    "status": "ok",
    "type": type,
    "page": page,
    "limit": limit
  }

# Default Query Parameter
@app.get("/users")
async def get_profile(path: str, role: str = 'user',):
  return {
    "status": "ok",
    "path": path,
    "role": role
  }

# Optional Query Parameter
@app.get("/posts")
async def get_posts(author: str, category: str | None = None):
  return {
    "status": "ok",
    "author": author,
    "category": category
  }

# Path Parameter & Query Parameter
@app.get("/category/{category_id}")
async def get_category(category_id: int, page: int = 1, limit: int = 10):
  return {
    "status": "ok",
    "category_id": category_id,
    "page": page,
    "limit": limit
  }
