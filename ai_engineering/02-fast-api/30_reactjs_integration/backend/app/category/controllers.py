"""Business logic for categories."""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.category.models import Category
from app.category.schemas import CategoryCreate, CategoryUpdate
from app.core.exceptions import ConflictError, NotFoundError
from app.product.models import Product


def get_category(db: Session, category_id: int) -> Category:
    category = db.get(Category, category_id)
    if category is None:
        raise NotFoundError(f"Category {category_id} not found")
    return category


def list_categories(db: Session, skip: int = 0, limit: int = 100) -> list[Category]:
    stmt = select(Category).order_by(Category.name).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def _name_taken(db: Session, name: str, exclude_id: int | None = None) -> bool:
    stmt = select(Category.id).where(Category.name == name)
    if exclude_id is not None:
        stmt = stmt.where(Category.id != exclude_id)
    return db.scalar(stmt) is not None


def create_category(db: Session, data: CategoryCreate) -> Category:
    if _name_taken(db, data.name):
        raise ConflictError(f"Category '{data.name}' already exists")

    category = Category(**data.model_dump())
    db.add(category)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ConflictError(f"Category '{data.name}' already exists")
    db.refresh(category)
    return category


def update_category(db: Session, category_id: int, data: CategoryUpdate) -> Category:
    category = get_category(db, category_id)
    changes = data.model_dump(exclude_unset=True)

    new_name = changes.get("name")
    if new_name is not None and _name_taken(db, new_name, exclude_id=category_id):
        raise ConflictError(f"Category '{new_name}' already exists")

    for field, value in changes.items():
        setattr(category, field, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ConflictError("Category could not be updated due to a conflict")
    db.refresh(category)
    return category


def delete_category(db: Session, category_id: int) -> None:
    category = get_category(db, category_id)

    has_products = db.scalar(
        select(Product.id).where(Product.category_id == category_id).limit(1)
    )
    if has_products is not None:
        raise ConflictError("Cannot delete a category that still has products")

    db.delete(category)
    db.commit()
