from util.performance.mem_measurement import *
from util.performance.time_measurement import *
from util.performance.summary import *
from util.rand import generate_random_array

from typing import List


# merge two lists into one
def __merge(first: List[int], second: List[int]) -> List[int]:
    ans = []
    for _ in range(len(first) + len(second)):
        if len(first) > 0 and len(second) > 0:
            if first[0] < second[0]:
                ans += [first.pop(0)]
            else:
                ans += [second.pop(0)]
        elif len(first) > 0:
            ans += [first.pop(0)]
        elif len(second) > 0:
            ans += [second.pop(0)]
    return ans


# sort
def merge_sort(a: List[int]) -> List[int]:
    if len(a) > 1:
        return __merge(merge_sort(a[:len(a) // 2]), merge_sort(a[len(a) // 2:]))

    return a


if __name__ == "__main__":
    start_mem_trace()

    arr = generate_random_array(2 * 10 ** 4, (-10 ** 9, 10 ** 9))

    time, ans = get_function_execution_time_sec(merge_sort, arr)

    with open("io_folder/output.txt", "w") as file:
        file.write(" ".join(map(str, ans)))

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
