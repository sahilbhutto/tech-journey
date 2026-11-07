from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

# Pydantic model for auth header
class AuthHeaders(BaseModel):
    model_config = {"extra": "forbid"}
    api_key: str
    roles: list[str] = []


# User-Agent & Request-ID headers
@app.get("/profile")
async def get_profile(
    user_agent: Annotated[str | None, Header()] = None,
    request_id: Annotated[str | None, Header()] = None,
):
    return {
        "user_agent": user_agent,
        "request_id": request_id,
    }

# Multiple values for the same header
@app.get("/products")
async def get_products(
    tags: Annotated[list[str] | None, Header()] = None,
):
    return {
        "message": "Product tags received",
        "tags": tags,
    }

# Headers using a Pydantic model
@app.get("/users")
async def get_users(
    headers: Annotated[AuthHeaders, Header()],
):
    return {
        "api_key": headers.api_key,
        "roles": headers.roles,
        "message": "User headers received",
    }
