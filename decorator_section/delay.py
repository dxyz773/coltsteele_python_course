from functools import wraps
from time import sleep


def delay(time):

    def decorator(fn):
        @wraps(fn)
        def create_delay(*args, **kwargs):
            print(f"Waiting {time}s before running {fn.__name__}")
            sleep(time)
            return fn(*args, **kwargs)

        return create_delay

    return decorator
