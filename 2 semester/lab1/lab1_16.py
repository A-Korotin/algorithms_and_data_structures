import random

from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *
import sys


def main():
    with open("input.txt", 'r') as f_in:
        n = int(f_in.readline().strip())
        dist = [list(map(int, f_in.readline().split())) for _ in range(n)]

    # dp[S][i] - кратчайший путь, заканчивающийся в i, проходящий по всем вершинам множества S (S - битовая маска)
    dp = [[sys.maxsize] * n for _ in range(1 << n)]
    dp[1][0] = 0

    for S in range(1, 1 << n, 2):
        for i in range(n):
            if not S & (1 << i):
                continue
            for j in range(n):
                if S & (1 << j):
                    dp[S][i] = min(dp[S][i], dp[S ^ (1 << i)][j] + dist[j][i])

    # Построение пути
    path = []
    S = (1 << n) - 1
    cur = 0
    for i in range(n - 1, 0, -1):
        min_prev = sys.maxsize
        next_city = None
        for j in range(n):
            if S & (1 << j):
                if dp[S][j] + dist[j][cur] < min_prev:
                    min_prev = dp[S][j] + dist[j][cur]
                    next_city = j
        path.append(cur)
        cur = next_city
        S ^= (1 << cur)
    path.append(cur)

    d = 0
    for i in range(n-1):
        d += dist[path[i]][path[i+1]]

    print(d)
    print(*[p + 1 for p in path])


if __name__ == "__main__":
    with open("input.txt", 'w') as f:
        n = 13
        dist = []
        for i in range(n):
            dist.append([None for _ in range(n)])

        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dist[i][j] = 0
                    continue
                num = random.randint(0, 10**6)
                dist[i][j] = num
                dist[j][i] = num

        f.write(f"{n}\n")
        for row in dist:
            f.write(" ".join(map(str, row)) + "\n")

    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)