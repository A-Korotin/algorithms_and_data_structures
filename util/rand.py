from random import randint
from typing import List, Tuple


def generate_random_array(n: int, number_range: Tuple[int, int] = (1, 10)) -> List[int]:
    lower, upper = number_range
    return [randint(lower, upper) for _ in range(n)]
