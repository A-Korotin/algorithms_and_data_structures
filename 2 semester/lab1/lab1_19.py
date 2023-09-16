from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float("inf")
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print("A", i, end=" ", sep="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")


def main():
    with open("input.txt", 'r') as f_in:
        n = int(f_in.readline())
        p = []
        for i in range(n):
            a, b = map(int, f_in.readline().split())
            p.append(a)
        p.append(b)

    m, s = matrix_chain_order(p)
    print_optimal_parens(s, 1, n)
    print()


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)