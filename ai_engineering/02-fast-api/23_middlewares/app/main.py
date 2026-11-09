from fastapi import FastAPI
from middlewares import first_middleware, second_middleware, users_only_middleware, CustomLoggingMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# Built-in middleware
app.add_middleware(HTTPSRedirectMiddleware)

# Register custom ASGI middleware
app.add_middleware(
    CustomLoggingMiddleware,
    prefix="CUSTOM LOG"
)


app.middleware("http")(first_middleware)
app.middleware("http")(second_middleware)
app.middleware("http")(users_only_middleware)


@app.get("/products")
def get_products():
    print("Inside: get_products endpoint")
    return {
        "data": ["macbook", "watch", "mobile", "laptop"]
    }

@app.get("/users")
def get_users():
    print("Inside: get_users endpoint")
    return {
        "data": ["sahil", "rehman", "fardeen", "farhan"]
    }
