from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def count_patterns(M, N):
    memo = {}

    def dp(memo, row, mask, prev):
        if row == M:
            return 1
        if (row, mask, prev) in memo:
            return memo[(row, mask, prev)]
        ans = 0
        for cur in range(1 << N):
            ok = True
            for shift in range(1):
                if (cur & (prev >> shift) & 1) and (cur & (mask >> shift) & 1):
                    ok = False
            if ok:
                ans += dp(memo, row+1, mask^cur, cur)
        memo[(row, mask, prev)] = ans
        return ans

    ans = dp(memo, 0, 0, 0)
    if M == 1 or N == 1:
        return ans

    return ans + 2


def main():
    # Чтение входных данных
    with open('input.txt', 'r') as f:
        m, n = map(int, f.readline().split())

    ans = count_patterns(m, n)

    print(ans)


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
