from fastapi import APIRouter, HTTPException

router = APIRouter()


categories = [
    {"id": 1, "name": "Electronics"},
    {"id": 2, "name": "Clothing"},
    {"id": 3, "name": "Groceries"},
    {"id": 4, "name": "Furniture"},
]


@router.get("/")
def get_categories():
    return categories


@router.get("/{category_id}")
def get_category(category_id: int):

    for category in categories:
        if category["id"] == category_id:
            return category

    raise HTTPException(
        status_code=404,
        detail="Category not found"
    )
