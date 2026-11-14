"""Model registry: import every model so it is attached to `Base.metadata`.

Alembic's env.py imports this module for autogenerate. Add new models here.
"""

from app.category.models import Category  # noqa: F401
from app.db.base import Base  # noqa: F401
from app.product.models import Product  # noqa: F401
