from fastapi import APIRouter, HTTPException

router = APIRouter()

users = [
    {"id": 1, "name": "Sahil", "email": "sahil@example.com"},
    {"id": 2, "name": "Ali", "email": "ali@example.com"},
    {"id": 3, "name": "Ahmed", "email": "ahmed@example.com"},
    {"id": 4, "name": "Sara", "email": "sara@example.com"},
]


@router.get("/")
def get_users():
    return users


@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
