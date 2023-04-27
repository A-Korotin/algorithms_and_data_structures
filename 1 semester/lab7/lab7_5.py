from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def main():
    with open("io_folder/input.txt") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))
        m = int(f.readline())
        b = list(map(int, f.readline().split()))
        l = int(f.readline())
        c = list(map(int, f.readline().split()))

    dp = [[[0 for _ in range(l + 1)] for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    with open("io_folder/output.txt", "w") as f:
        f.write(str(dp[n][m][l]))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
