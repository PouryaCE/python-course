from functools import wraps


def max_result(thereshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > thereshold:
                print("Result is too large ({0}). Max allowed ({1})".format(result, thereshold))
            return result
        return wrapper
    return decorator



@max_result(125)
def cube(n):
    return n **3

cube(6)