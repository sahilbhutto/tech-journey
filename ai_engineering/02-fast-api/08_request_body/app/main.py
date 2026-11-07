from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
  name: str
  price: float
  stock: int | None = None
  

@app.post("/products")
async def create_products(product_data: Product):
  print(product_data.name)
  print(product_data.price)
  print(product_data.stock)
  return {
    "response": "Product created successfully",
    "data": product_data
  }
