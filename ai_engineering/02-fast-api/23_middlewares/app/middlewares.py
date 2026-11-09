from fastapi import Request


async def first_middleware(request: Request, call_next):
    print("1st Middlware: before processing request")

    response = await call_next(request)

    print("1st Middlware: after processing request & before returning response")

    return response


async def second_middleware(request: Request, call_next):
    print("2nd Middlware: before processing request")

    response = await call_next(request)

    print("2nd Middlware: after processing request & before returning response")

    return response


async def users_only_middleware(request: Request, call_next):
    if request.url.path.startswith("/users"):
        print("Url: ", request.url)
        print("User Middleware: before processing request")

        response = await call_next(request)

        print("User Middleware: after processing request")

        return response

    else:
        print("Users only middleware: This middleware is exist only for /users endpoints")
        response = await call_next(request)
        return response

class CustomLoggingMiddleware:
    def __init__(self, app, prefix="LOG"):
        self.app = app
        self.prefix = prefix

    async def __call__(self, scope, receive, send):

        # Only handle HTTP requests
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        # Before request
        print(f"{self.prefix}: Request Started")
        print("Method:", scope["method"])
        print("Path:", scope["path"])

        # Intercept response
        async def send_wrapper(message):

            if message["type"] == "http.response.start":
                print(f"{self.prefix}: Response Started")
                print("Status Code:", message["status"])

            await send(message)

        # Call next ASGI application
        await self.app(scope, receive, send_wrapper)

        # After response
        print(f"{self.prefix}: Request Completed")
