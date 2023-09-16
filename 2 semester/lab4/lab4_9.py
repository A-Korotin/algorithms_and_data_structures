from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def z_func(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i] - 1
    return z


def calc_next(ln, k, prev, n):
    res = k + 2 + len(str(ln // k))
    if ln == k:
        res -= 2
    if prev == n:
        res -= 1
    return res


def main():
    with open("input.txt", "r") as input_file:
        s = input_file.readline().strip()

    n = len(s)
    s += '_'
    dp = [n - i for i in range(n + 1)]
    next = [[n - i, n - i] for i in range(n + 1)]
    for i in range(n - 2, -1, -1):
        z = z_func(s[i:])
        if dp[i] > dp[i + 1] + 2:
            dp[i] = dp[i + 1] + 2
            next[i] = [1, 1]
        for j in range(i + 1, n + 1):
            k = 1
            while k ** 2 <= j - i:
                if (j - i) % k:
                    k += 1
                    continue
                if z[k] + k >= j - i and dp[i] > dp[j] + calc_next(j - i, k, j, n):
                    dp[i] = dp[j] + calc_next(j - i, k, j, n)
                    next[i] = [j - i, k]
                if z[(j - i) // k] + (j - i) // k >= j - i and dp[i] > dp[j] + calc_next(j - i, (j - i) // k, j, n):
                    dp[i] = dp[j] + calc_next(j - i, (j - i) // k, j, n)
                    next[i] = [j - i, (j - i) // k]
                k += 1

    with open('output.txt', 'w') as out:
        i = 0
        while i < n:
            start, end = next[i]
            if i > 0:
                out.write('+')
            out.write(s[i: i + end])
            if start != end:
                out.write('*' + str(start // end))
            i += next[i][0]


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
