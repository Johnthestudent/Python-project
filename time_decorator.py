from typing import Dict
from timeit import default_timer as timer
import time

execution_time: Dict[str, float] = {}


def time_decorator(fn):
    """
    Code returns a `time_decorator`
    which calculates decorated function execution time
    and puts this time value to `execution_time` dictionary where `key` is
    decorated function name and `value` is this function execution time.
    """

    def func_add(a, b, sleep_time):
        sleep_time = time.sleep(0.2)
        start = timer()
        print(a + b)
        end = timer()
        time_of_it = end - start
        execution_time = dict([(fn.__name__, time_of_it)])
        return execution_time
        func(a, b, sleep_time)
    return func_add


@time_decorator
def func_add(a: int, b: int, sleep_time: int) -> int:
    return a + b

