from util.performance.mem_measurement import get_max_mem_usage_mb, start_mem_trace
from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.summary import print_time_and_mem_usage_summary

from typing import List, Tuple


def insertion_sort_with_indices(inp: List[int]) -> Tuple[List[int], List[int]]:
    arr = inp.copy()
    indices = {}
    for j in range(0, len(arr)):
        tmp = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > tmp:
            arr[i + 1] = arr[i]
            i -= 1
        indices[tmp] = i + 2
        arr[i + 1] = tmp

    return arr, [indices[i] for i in inp]


if __name__ == "__main__":
    start_mem_trace()

    with open("io_folder/input.txt", "r") as file:
        _ = int(file.readline())
        arr = list(map(int, file.readline().split(" ")))

    time, answer = get_function_execution_time_sec(insertion_sort_with_indices, arr)

    with open("io_folder/output.txt", "w") as file:
        file.write(" ".join(map(str, answer[1])))
        file.write("\n")
        file.write(" ".join(map(str, answer[0])))

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
