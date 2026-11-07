from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Define Emum for Product Category
class ProductCategory(str, Enum):
  electronics = "electronics"
  books = "books"
  cloths = "cloths"

# GET - Get All Products
@app.get("/products")
async def get_products():
  return {
    "response": "Fetched all products",
    "products": [
    {
      "name": "Laptop",
      "price": 1200,
    },
    {
      "name": "Keybord",
      "price": 50
    }
    ]
  }

# GET - Get Single Product
@app.get("/products/{produc_id}")
async def get_product(product_id: int):
  return {
    "response": "Fetch product",
    "product": product_id
  }

# Post - Create Product
@app.post("/products")
async def create_product(product_data: dict):
  return {
    "response": "Product created",
    "new_product": product_data
  }

# Put - Update Product
@app.put("/products/{product_id}")
async def update_product(product_id: int, product_data: dict):
  return {
    "response": f"Product updated with id {product_id}",
    "updated_product": product_data
  }

# Patch - Partialy Update Product
@app.patch("/products/{product_id}")
async def partialy_update_product(product_id: int, product_data: dict):
  return {
    "response": f"Partialy product updated with id: {product_id}",
    "updated_product": product_data
  }

# Delete -  Delete Product
@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
  return {
    "response": f"Product deleted with id {product_id}",
  }

# Get - Product by Categeory - Predefined Values
@app.get("/products/category/{category}")
async def get_products_by_category(category: ProductCategory):
  return {
    "response": "Fetched products by category",
    "cateogry": category
  }
