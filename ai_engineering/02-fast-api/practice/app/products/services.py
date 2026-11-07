from app.products.models import Product
from app.db.config import async_session

async def create_product():
    async with async_session() as session:
        pass
