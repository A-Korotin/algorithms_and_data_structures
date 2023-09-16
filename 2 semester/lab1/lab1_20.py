from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def count_almost_palindromes(n, k, s):
    # инициализация динамики
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1  # строка/столбец длины 1 - палиндром
        if i < n - 1 and s[i] == s[i + 1]:
            dp[i][i + 1] = 1  # строка/столбец длины 2 - палиндром

    # пересчет динамики
    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

    # подсчет почти палиндромов
    count = 0
    for i in range(n):
        for j in range(i, n):
            if dp[i][j] <= k:
                count += 1

    return count


def main():
    with open("input.txt", 'r') as f_in:
        n, k = map(int, f_in.readline().split())
        s = f_in.readline().strip()

    print(n, k)
    print(s)
    ans = count_almost_palindromes(n, k, s)

    print(ans)


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
