from fastapi import FastAPI, Cookie
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

class ProductCookies(BaseModel):
    model_config = {"extra": "forbid"}
    session_id: str
    prefered_category: str | None = None
    tracking_id: str | None = None


@app.get("/products/recommendations")
async def get_recommended_products(
    session_id: Annotated[str | None, Cookie()] = None
):
    if session_id:
        return {
            "response": f"Recommended products with session_id: {session_id}",
            "session_id": session_id,
        }

    return {
        "response": "Default products",
    }


@app.get("/products/recommendated")
async def get_recommendations(
    cookies: Annotated[ProductCookies, Cookie()]
):
    if not cookies.session_id:
        return {"message": "No session found"}

    if cookies.prefered_category and cookies.tracking_id:
        return {
            "session_id": cookies.session_id,
            "preferred_category": cookies.prefered_category,
            "tracking_id": cookies.tracking_id,
        }

    return {
        "session_id": cookies.session_id,
        "preferred_category": cookies.prefered_category,
        "tracking_id": cookies.tracking_id,
    }
