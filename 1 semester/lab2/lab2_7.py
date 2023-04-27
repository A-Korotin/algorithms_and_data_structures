from util.performance.mem_measurement import *
from util.performance.time_measurement import *
from util.performance.summary import *
from util.rand import generate_random_array

from typing import List


def max_sub_array(array: List[int]) -> List[int]:
    max_sum = 0
    current_sum = 0
    start_max = 0
    sub_array_candidates = []
    for i in range(len(array)):
        if current_sum <= 0:
            start_max = i
            current_sum = 0
        current_sum += array[i]
        if current_sum > max_sum:
            max_sum = current_sum
            sub_array_candidates.append((start_max, i))

    tmp_max_array = array[sub_array_candidates[0][0]: sub_array_candidates[0][1] + 1]
    for start, i2 in sub_array_candidates:
        if sum(array[start: i2 + 1]) > sum(tmp_max_array):
            tmp_max_array = array[start: i2 + 1]
    return tmp_max_array


if __name__ == "__main__":
    start_mem_trace()

    arr = generate_random_array(10, (-5, 5))
    print(arr)

    with open("io_folder/output.txt", "w") as file:
        time, ans = get_function_execution_time_sec(max_sub_array, arr)
        file.write(" ".join(map(str, ans)))
        print(ans)

    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
