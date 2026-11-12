from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.category.routers import router as category_router
from app.core.exceptions import register_exception_handlers
from app.db.config import settings
from app.product.routers import router as product_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG,
        lifespan=lifespan,
        docs_url="/docs" if settings.ENVIRONMENT != "production" else None,
        redoc_url="/redoc" if settings.ENVIRONMENT != "production" else None,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials="*" not in settings.CORS_ORIGINS,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)

    app.include_router(category_router, prefix=settings.API_V1_PREFIX)
    app.include_router(product_router, prefix=settings.API_V1_PREFIX)

    @app.get("/health", tags=["Health"])
    def health() -> dict[str, str]:
        return {"status": "ok"}

    return app


app = create_app()
