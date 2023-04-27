from time import time
from typing import Tuple, Callable, Any


def get_function_execution_time_sec(method: Callable, *args) -> Tuple[float, Any]:
    start = time()
    func_return_value = method(*args)

    return time() - start, func_return_value
