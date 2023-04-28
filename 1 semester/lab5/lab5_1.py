import random

from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *
from typing import List


def check_heap(a: List[int]) -> bool:
    is_heap = True
    n = len(a)
    for i in range(n):
        if 2 * i + 1 < n and a[i] > a[2 * i + 1]:
            is_heap = False
            break
        if 2 * i + 2 < n and a[i] > a[2 * i + 2]:
            is_heap = False
            break
    return is_heap


def main():
    with open("io_folder/input.txt", 'r') as file:
        _ = int(file.readline())
        inp = list(map(int, file.readline().split()))

    with open('io_folder/output.txt', 'w') as file:
        file.write("YES" if check_heap(inp) else "NO")


if __name__ == '__main__':
    start_mem_trace()
    with open("io_folder/input.txt", 'w') as file:
        file.write(f"{10**6}\n")
        file.write(f'{" ".join([f"{random.randint(-2*10**9, 2* 10**9)}" for _ in range(10**6)])}')

    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
