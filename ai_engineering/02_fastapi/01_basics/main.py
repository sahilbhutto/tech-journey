from fastapi import FastAPI, Depends  # type: ignore

app = FastAPI()

def get_current_user():
    user = {
        "id": 101,
        "name": "Sahil",
        "role": "developer"
    }

    return user

@app.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return {
        "message": "Profile accessed successfully",
        "user": user
    }

@app.get("/orders")
def get_orders(user=Depends(get_current_user)):
    return {
        "user_id": user["id"],
        "orders": ["Order 1", "Order 2"]
    }
