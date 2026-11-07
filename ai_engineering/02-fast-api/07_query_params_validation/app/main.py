from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

PRODUCTS = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Mobile", "price": 40000},
    {"id": 3, "name": "Mouse", "price": 1200}
]

# Validation without Annotated
@app.get("/products")
async def get_products(search: str | None = Query(default=None, max_length=8)):
  if search:
    lower_search = search.lower()
    filter_products = []

    for product in PRODUCTS:
      if lower_search in product["name"].lower():
        filter_products.append(product)
    return filter_products
  return PRODUCTS


# Validation with Annotated
@app.get("/shop/products")
async def get_products(search: Annotated[str, Query(max_length=8)]=None):
   if search:
      lower_search = search.lower()
      filter_products = []

      for product in PRODUCTS:
        if lower_search in product["name"].lower():
          filter_products.append(product)
      return filter_products
   return PRODUCTS

