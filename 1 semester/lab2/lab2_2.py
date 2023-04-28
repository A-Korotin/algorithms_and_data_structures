from util.performance.mem_measurement import *
from util.performance.time_measurement import *
from util.performance.summary import *
from util.rand import generate_random_array

from typing import List, IO
from sys import stdout


def __merge(array: List[int], p: int, q: int, r: int, file: IO = stdout) -> None:
    first = []
    second = []
    for i in range(p, q):
        first.append(array[i])
    for j in range(q, r):
        second.append(array[j])
    for i in range(len(first) + len(second)):
        if len(first) > 0 and len(second) > 0:
            if first[0] < second[0]:
                array[p + i] = (first.pop(0))
            else:
                array[p + i] = (second.pop(0))
        elif len(first) > 0:
            array[p + i] = (first.pop(0))
        elif len(second) > 0:
            array[p + i] = (second.pop(0))

    file.write(f"{p + 1} {r} {array[p]} {array[r - 1]}\n")


def merge_sort(array: List[int], p: int, r: int, file: IO = stdout) -> None:
    if p < r and r - p > 1:
        q = (p + r) // 2
        merge_sort(array, p, q, file)
        merge_sort(array, q, r, file)
        __merge(array, p, q, r, file)


if __name__ == "__main__":
    start_mem_trace()

    arr = generate_random_array(2*10**4, (-10 ** 9, 10 ** 9))
    with open("io_folder/output.txt", "w") as file:
        time, _ = get_function_execution_time_sec(merge_sort, arr, 0, len(arr), file)
        file.write(" ".join(map(str, arr)))

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
