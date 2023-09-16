from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def h_function(s, a, m1, m2):
    n = len(s) + 1
    h = [(0, 0)] * n
    for i in range(1, n):
        number = ord(s[i - 1])
        h_1 = (a * h[i - 1][0] + number) % m1
        h_2 = (a * h[i - 1][0] + number) % m2
        h[i] = (h_1, h_2)
    return h


def main():

    m1, m2 = 10 ** 9 + 7, 10 ** 9 + 9
    with open('input.txt', 'r') as file, open('output.txt', 'w') as out:
        s = file.readline().strip()
        q = int(file.readline())

        h = h_function(s, 12, m1, m2)
        for _ in range(q):
            a, b, l = map(int, file.readline().split())
            h11 = (h[a + l][0] - (12 ** l) * h[a][0]) % m1
            h21 = (h[b + l][0] - (12 ** l) * h[b][0]) % m1
            h12 = (h[a + l][1] - (12 ** l) * h[a][1]) % m2
            h22 = (h[b + l][1] - (12 ** l) * h[b][1]) % m2

            if h11 == h12 and h12 == h21 and h21 == h22:
                out.write("Yes\n")
            else:
                out.write("No\n")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
