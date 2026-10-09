from fastapi import FastAPI, Request # type: ignore
from fastapi.responses import JSONResponse # type: ignore

app = FastAPI()

SECRET_TOKEN = "my-secret-token"

@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")

    if token != SECRET_TOKEN:
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )

    return await call_next(request)

@app.get("/profile")
def profile():
    return {"message": "Welcome to your profile!"}
