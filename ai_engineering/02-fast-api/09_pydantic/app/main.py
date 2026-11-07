from fastapi import FastAPI, status
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()

# User Model
class User(BaseModel):
    username: str = Field(min_length=3, max_length=30)
    email: EmailStr
    password: str = Field(min_length=8)
    role: str = "user"

# Product Model
class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    description: str = Field(min_length=10, max_length=200)
    price: float = Field(gt=0)
    stock: int = Field(ge=0, default=0)

# Address Model
class Address(BaseModel):
    city: str
    country: str

# Order Model
class Order(BaseModel):
    customer: User
    shipping_address: Address
    ordered_products: list[Product]


# Create User
@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "username": user.username,
        "email": user.email,
        "role": user.role
    }

# Create Product
@app.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    return {
        "message": "Product created successfully",
        "data": product
    }

# Create Order
@app.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: Order):
    return {
        "message": "Order created successfully",
        "data": order
    }
