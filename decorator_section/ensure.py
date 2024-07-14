from functools import wraps


def ensure_first_thing_is(value):
    def decorator(fn):
        @wraps(fn)
        def ensure(*args, **kwargs):
            if args[0] == value:
                return fn(*args, **kwargs)
            else:
                return f"First argument is NOT {value}"

        return ensure

    return decorator


@ensure_first_thing_is("burrito")
def fav_foods(*foods):
    print(*foods)


@ensure_first_thing_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(fav_foods("bananas", "burrito"))
print(add_to_ten(10.0, 10))
