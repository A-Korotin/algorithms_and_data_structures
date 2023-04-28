from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.mem_measurement import *
from util.performance.time_measurement import *
from util.rand import generate_random_array

from random import randint
from typing import List, Tuple


def p(arr: List[int]) -> int:
    x = arr[0]
    i = 0
    for j in range(1, len(arr)):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[0], arr[i] = arr[i], arr[0]
    return i


def rand_qsort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    k = randint(1, len(arr) - 1)
    arr[0], arr[k] = arr[k], arr[0]
    j = p(arr)
    left = rand_qsort(arr[:j])
    right = rand_qsort(arr[j + 1:])
    return left + [arr[j]] + right


def p3(arr: List[int], pivot: int) -> Tuple[List[int], List[int], List[int]]:
    less, equal, greater = [], [], []
    for element in arr:
        if element < pivot:
            less.append(element)
        if element == pivot:
            equal.append(element)
        if element > pivot:
            greater.append(element)
    return less, equal, greater


def rand_qsort_3(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    less, equal, greater = p3(arr, arr[randint(1, len(arr) - 1)])
    return rand_qsort_3(less) + equal + rand_qsort_3(greater)


def gen_test_arrays(n: int) -> Tuple[List[int], List[int], List[int]]:
    sor = sorted(generate_random_array(n, (-10**9, 10**9)))
    rand = generate_random_array(n, (-10**9, 10**9))
    rev = sorted(generate_random_array(n, (-10**9, 10**9)), reverse=True)
    return rev, sor, rand

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
    n_ranges = (10**3, 10**4, 7*10**4)
    labels = ("reversed", "sorted", "random")

    for n in n_ranges:
        print(f"{n}\n\n")
        for i, arr in enumerate(gen_test_arrays(n)):
            start_mem_trace()
            time, ans = get_function_execution_time_sec(merge_sort, arr)
            print(f'{labels[i]}')
            mem = get_max_mem_usage_mb()
            print_time_and_mem_usage_summary(time, mem)

    # for n in n_ranges:
    #     print("\n\n")
    #     print("Partition " + str(n))
    #     for i, arr in enumerate(gen_test_arrays(n)):
    #         start_mem_trace()
    #         time, ans = get_function_execution_time_sec(rand_qsort, arr)
    #         print(labels[i])
    #         mem = get_max_mem_usage_mb()
    #         print_time_and_mem_usage_summary(time, mem)
    #     print("\n\n")
    #     print("Partition 3 " + str(n))
    #     for i, arr in enumerate(gen_test_arrays(n)):
    #         start_mem_trace()
    #         time, ans = get_function_execution_time_sec(rand_qsort_3, arr)
    #         print(labels[i])
    #         mem = get_max_mem_usage_mb()
    #         print_time_and_mem_usage_summary(time, mem)

