from functools import wraps


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)

    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y


print(add(3, 5))
print(add.__doc__)
