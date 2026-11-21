from fastapi import APIRouter
from app.account.services import create_user
from app.db.config import SessionDepends


router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/register")
async def register(session: SessionDepends, name: str, email: str):
    return await create_user(session, name, email)
