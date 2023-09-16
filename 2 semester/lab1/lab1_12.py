import random

from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def split_sequence(n, seq):
    total_sum = sum(seq)
    if total_sum % 2 != 0:
        return -1, []

    s = total_sum // 2
    table = [[False for _ in range(s + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        table[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            table[i][j] = table[i - 1][j]
            if j >= seq[i - 1]:
                table[i][j] = table[i][j] or table[i - 1][j - seq[i - 1]]

    if not table[n][s]:
        return -1, []

    split = []
    i, j = n, s
    while i > 0 and j > 0:
        if table[i - 1][j]:
            i -= 1
        elif table[i - 1][j - seq[i - 1]]:
            split.append(i)
            j -= seq[i - 1]
            i -= 1

    return len(split), split[::-1]


def main():
    with open("input.txt", 'r') as f_in:
        n = int(f_in.readline())
        sequence = list(map(int, f_in.readline().split()))

    with open("output.txt", 'w') as f_out:
        a, b = split_sequence(n, sequence)
        f_out.write(f'{a}\n')
        if a != -1:
            f_out.write(" ".join(map(str, b)))


if __name__ == "__main__":
    with open("input.txt", 'w') as f_in:
        n = 40_000
        f_in.write(f'{n}\n')
        f_in.write(" ".join(map(str, [random.randint(1, i) for i in range(1, n+1)])))

    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)