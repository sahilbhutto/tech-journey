
from functools import wraps


def logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        print(f"Calling: {func.__name__}")
        print(f"Arguments: {args}")
        print(f"Keyword Arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Result: {result}")

        return result

    return wrapper


@logger
def create_user(name, age, role="user"):
    return {
        "name": name,
        "age": age,
        "role": role
    }


user = create_user("Sahil", 21, role="developer")

print("\nUser:")
print(user)
