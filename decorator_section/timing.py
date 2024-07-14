from time import time
from functools import wraps


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time elapsed {end - start}")
        return result

    return wrapper


@speed_test
def sum_nums():
    return sum(x for x in range(1000000))


sum_nums()


# CHECK SECTION 12 100 DAys of python to start
