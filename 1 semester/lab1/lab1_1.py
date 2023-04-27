from util.performance.mem_measurement import get_max_mem_usage_mb, start_mem_trace
from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.summary import print_time_and_mem_usage_summary
from util.rand import generate_random_array

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    for j in range(1, len(arr)):
        tmp = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > tmp:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = tmp

    return arr


def setup_input_array(n: int) -> None:
    with open("io_folder/input.txt", "w") as file:
        file.write(f"{n}\n")
        file.write(" ".join(map(str, generate_random_array(n, number_range=(-100, 100)))))


if __name__ == "__main__":
    start_mem_trace()
    setup_input_array(1000)

    with open("io_folder/input.txt", "r") as file:
        _ = int(file.readline())
        arr = list(map(int, file.readline().split(" ")))

    time, answer = get_function_execution_time_sec(insertion_sort, arr)

    with open("io_folder/output.txt", "w") as file:
        file.write(" ".join(map(str, answer)))

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
