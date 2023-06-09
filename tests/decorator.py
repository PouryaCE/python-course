from timeit import default_timer
from functools import wraps


def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = default_timer()
        result = func(*args, **kwargs)
        print("function name:", func.__name__, "|  took :", default_timer() - t)
        return result
    return wrapper




def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print("Result is too large ({0}). Max allowed 100".format(result))
        return result
    return wrapper





@measure
@max_result
def cube(n):
    return n ** 3

print(cube(6))
print(cube.__name__)