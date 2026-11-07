from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

users = {
    1: "Sahil",
    2: "John",
    3: "Zeb"
}


# 1. HTTPException
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user_id": user_id, "name": users[user_id]}


# 2. Custom exception
class UserBlockedException(Exception):
    pass


@app.get("/blocked-user")
async def blocked_user():
    raise UserBlockedException("This user is blocked")


# 3. Custom exception handler
@app.exception_handler(UserBlockedException)
async def handle_blocked_user(request: Request, exc: UserBlockedException):
    return JSONResponse(
        status_code=403,
        content={"error": str(exc)},
    )


# 4. Override the default HTTPException handler
@app.exception_handler(HTTPException)
async def handle_http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
