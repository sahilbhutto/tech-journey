from fastapi import FastAPI, status

app = FastAPI()

# HTTP STATUS CODES
# 100 - 199: INFORMATIONAL
# 200 - 299: SUCCESS
# 300 - 399: REDIRECTION
# 400 - 499: CLIENT ERROR
# 500 - 599: SERVER ERROR

# 200 OK - SUCCESS
# 201 CREATED - SUCCESS
# 204 NO CONTENT - SUCCESS
# 400 BAD REQUEST - CLIENT ERROR
# 404 NOT FOUND - CLIENT ERROR

products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Mobile", "price": 40000}
]


# GET - GET ALL PRODUCTS
@app.get("/products", status_code=status.HTTP_200_OK)
def get_products():
    return products


# GET - GET SINGLE PRODUCT
@app.get("/products/{product_id}", status_code=status.HTTP_200_OK)
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}


# POST - CREATE PRODUCT
@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(product: dict):
    products.append(product)
    return product


# PUT - UPDATE ENTIRE PRODUCT
@app.put("/products/{product_id}", status_code=status.HTTP_200_OK)
def update_product(product_id: int, updated_product: dict):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products[index] = updated_product
            return updated_product

    return {"message": "Product not found"}


# PATCH - PARTIALLY UPDATE PRODUCT
@app.patch("/products/{product_id}", status_code=status.HTTP_200_OK)
def partial_update_product(product_id: int, updated_data: dict):
    for product in products:
        if product["id"] == product_id:
            product.update(updated_data)
            return product

    return {"message": "Product not found"}


# DELETE - DELETE PRODUCT
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return

    return {"message": "Product not found"}
