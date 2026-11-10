from fastapi import FastAPI
from app.cateogry.routers import router as category_routers
from app.product.routers import router as product_routers
from app.user.routers import router as user_routers


app = FastAPI()

app.include_router(category_routers, prefix="/categories" ,tags=["cateogories"])
app.include_router(product_routers, prefix="/products" ,tags=["products"])
app.include_router(user_routers, prefix="/users" ,tags=["users"])
