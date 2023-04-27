from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *

from typing import List


def radix_sort(arr: List[str], k: int):
    arr = arr[::-1]
    indexes = list(range(len(arr[0])))
    for i in range(k):
        available_chars = dict()
        for code in range(97, 122 + 1):
            available_chars[chr(code)] = []

        vertical_line = ''.join([arr[i][j] for j in indexes])
        for index, value in enumerate(vertical_line):
            available_chars[value].append(indexes[index])
        indexes = []
        for value in available_chars.values():
            indexes.extend(value)

    for i in indexes:
        yield i+1


if __name__ == "__main__":
    start_mem_trace()
    k: int
    inp: list
    with open("io_folder/input.txt", 'r') as file:
        header = file.readline()
        *_, k = header.split(' ')
        k = int(k)
        inp = file.readlines()

    with open('io_folder/output.txt', 'w') as file:
        time, answer = get_function_execution_time_sec(radix_sort, inp, k)
        file.write(' '.join(map(str, answer)))

    max_mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, max_mem)
