from util.rand import generate_random_array
from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *

from typing import List


def get_h_index(citations: List[int]) -> int:
    citations = sorted(citations, reverse=True)
    for idx, item in enumerate(citations, 1):
        if idx > item:
            return idx - 1


if __name__ == "__main__":
    start_mem_trace()
    arr = generate_random_array(5000, (0, 1000))
    time, ans = get_function_execution_time_sec(get_h_index, arr)
    print(ans)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
