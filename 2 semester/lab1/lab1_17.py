from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def count_phone_numbers(N):
    MOD = 10 ** 9

    dp = [[0] * 10 for _ in range(N + 1)]
    for j in range(1, 10):
        dp[1][j] = 1 if j not in [0, 8] else 0

    for i in range(2, N + 1):
        dp[i][1] = (dp[i - 1][6] + dp[i - 1][8]) % MOD
        dp[i][2] = (dp[i - 1][7] + dp[i - 1][9]) % MOD
        dp[i][3] = (dp[i - 1][4] + dp[i - 1][8]) % MOD
        dp[i][4] = (dp[i - 1][3] + dp[i - 1][9] + dp[i - 1][0]) % MOD
        dp[i][6] = (dp[i - 1][1] + dp[i - 1][7] + dp[i - 1][0]) % MOD
        dp[i][7] = (dp[i - 1][2] + dp[i - 1][6]) % MOD
        dp[i][8] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
        dp[i][9] = (dp[i - 1][2] + dp[i - 1][4]) % MOD
        dp[i][0] = (dp[i - 1][4] + dp[i - 1][6]) % MOD

    total_count = sum(dp[N]) % MOD
    return total_count


def main():
    with open("input.txt", "r") as f:
        N = int(f.readline().strip())

    result = count_phone_numbers(N)

    with open("output.txt", "w") as f:
        f.write(str(result))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)