from functools import wraps
from time import time


def log_execution_time(func):
    """
    Decorator function that prints how long it took to execute the function
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        return_value = func(*args, **kwargs)
        end = time()
        delta = end - start
        print(f"Executing {func.__name__} took {delta} seconds.")
        return return_value
    return wrapper

def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 1 else n

timed_fib = log_execution_time(fib)