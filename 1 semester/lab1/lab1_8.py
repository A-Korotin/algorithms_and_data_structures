from util.performance.mem_measurement import get_max_mem_usage_mb, start_mem_trace
from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.summary import print_time_and_mem_usage_summary
from util.rand import generate_random_array
from typing import List
from io import FileIO


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left) + [pivot] + quick_sort(right)


def func(arr: List[int], file: FileIO) -> List[int]:
    sorted_arr = quick_sort(arr)
    n = len(arr)

    for i in range(n):
        if arr[i] != sorted_arr[i]:
            file.write(f"Swap elements at indices {i} and {arr.index(sorted_arr[i])}")
            arr[arr.index(sorted_arr[i])], arr[i] = arr[i], arr[arr.index(sorted_arr[i])]
    return arr


if __name__ == "__main__":
    start_mem_trace()

    arr = generate_random_array(5_000, (-10**9, 10**9))

    with open("io_folder/output.txt", "w") as file:
        time, answer = get_function_execution_time_sec(func, arr, file)

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
