from typing import Annotated

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.category import controllers
from app.category.schemas import CategoryCreate, CategoryRead, CategoryUpdate
from app.db.session import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

DbSession = Annotated[Session, Depends(get_db)]


@router.post("", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: DbSession):
    return controllers.create_category(db, payload)


@router.get("", response_model=list[CategoryRead])
def list_categories(
    db: DbSession,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=200)] = 100,
):
    return controllers.list_categories(db, skip=skip, limit=limit)


@router.get("/{category_id}", response_model=CategoryRead)
def get_category(category_id: int, db: DbSession):
    return controllers.get_category(db, category_id)


@router.patch("/{category_id}", response_model=CategoryRead)
def update_category(category_id: int, payload: CategoryUpdate, db: DbSession):
    return controllers.update_category(db, category_id, payload)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: int, db: DbSession):
    controllers.delete_category(db, category_id)
