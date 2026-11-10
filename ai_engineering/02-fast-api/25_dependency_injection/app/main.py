from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


async def get_current_user():
    return{
        "name": "Sahil Ali",
        "email": "sahil@gmail.com",
        "role": "admin",
    }


CurrentUserDependency = Annotated[dict, Depends(get_current_user),]


@app.get("/profile")
async def get_profile(user: CurrentUserDependency):
    return {
        "message": "Welcome to your profile",
        "user": user,
    }


@app.get("/checkout")
async def checkout_items(user: CurrentUserDependency):
    return {
        "message": "Checkout completed successfully",
        "customer": {
            "name": user["name"],
            "email": user["email"]
        },
    }
