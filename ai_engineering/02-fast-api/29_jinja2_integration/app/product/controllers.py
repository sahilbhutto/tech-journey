"""Business logic for products."""

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.category.models import Category
from app.core.exceptions import ConflictError, NotFoundError
from app.product.models import Product
from app.product.schemas import ProductCreate, ProductUpdate


def _ensure_category_exists(db: Session, category_id: int) -> None:
    if db.get(Category, category_id) is None:
        raise NotFoundError(f"Category {category_id} not found")


def _sku_taken(db: Session, sku: str, exclude_id: int | None = None) -> bool:
    stmt = select(Product.id).where(Product.sku == sku)
    if exclude_id is not None:
        stmt = stmt.where(Product.id != exclude_id)
    return db.scalar(stmt) is not None


def get_product(db: Session, product_id: int) -> Product:
    product = db.get(Product, product_id)
    if product is None:
        raise NotFoundError(f"Product {product_id} not found")
    return product


def list_products(
    db: Session,
    *,
    skip: int = 0,
    limit: int = 100,
    category_id: int | None = None,
    search: str | None = None,
    is_active: bool | None = None,
) -> list[Product]:
    stmt = select(Product)
    if category_id is not None:
        stmt = stmt.where(Product.category_id == category_id)
    if is_active is not None:
        stmt = stmt.where(Product.is_active == is_active)
    if search:
        pattern = f"%{search.strip()}%"
        stmt = stmt.where(Product.name.ilike(pattern) | Product.sku.ilike(pattern))
    stmt = stmt.order_by(Product.id).offset(skip).limit(limit)
    return list(db.scalars(stmt).all())


def create_product(db: Session, data: ProductCreate) -> Product:
    _ensure_category_exists(db, data.category_id)
    if _sku_taken(db, data.sku):
        raise ConflictError(f"SKU '{data.sku}' already exists")

    product = Product(**data.model_dump())
    db.add(product)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ConflictError(f"SKU '{data.sku}' already exists")
    db.refresh(product)
    return product


def update_product(db: Session, product_id: int, data: ProductUpdate) -> Product:
    product = get_product(db, product_id)
    changes = data.model_dump(exclude_unset=True)

    # These columns are NOT NULL; reject explicit nulls instead of hitting the DB.
    for required in ("name", "sku", "price", "stock", "is_active", "category_id"):
        if required in changes and changes[required] is None:
            raise ConflictError(f"'{required}' cannot be null")

    if "category_id" in changes:
        _ensure_category_exists(db, changes["category_id"])
    if "sku" in changes and _sku_taken(db, changes["sku"], exclude_id=product_id):
        raise ConflictError(f"SKU '{changes['sku']}' already exists")

    for field, value in changes.items():
        setattr(product, field, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ConflictError("Product could not be updated due to a conflict")
    db.refresh(product)
    return product


def delete_product(db: Session, product_id: int) -> None:
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()
