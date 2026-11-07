from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserRes(BaseModel):
    username: str
    email: str
    role: str

class User(UserRes):
    password: str
    

# 1. Return Type Annotation
@app.post("/users/signup")
async def signup_user(user: User) -> UserRes:
    return {
        "username": user.username,
        "email": user.email,
        "role": user.role,
    }


# 2. Response Model
@app.post("/users", response_model=UserRes)
async def create_user(user: User):
    return {
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "password": user.password,
    }


# 3. Include specific fields
@app.get("/profile", response_model=UserRes,
         response_model_include={"username", "email"})
async def get_profile():
    return {"username": "ali", "email": "ali@example.com", "role": "admin"}


# 4. Exclude specific fields
@app.get("/public-user", response_model=UserRes,
         response_model_exclude={"email"})
async def get_public_user():
    return {"username": "ali", "email": "ali@example.com", "role": "admin"}
