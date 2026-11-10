from fastapi import APIRouter, HTTPException

router = APIRouter()


products = [
    {"id": 1, "name": "MacBook", "price": 250000},
    {"id": 2, "name": "Laptop", "price": 120000},
    {"id": 3, "name": "Keyboard", "price": 5000},
    {"id": 4, "name": "Mouse", "price": 2500},
]


@router.get("/")
def get_products():
    return products


@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
