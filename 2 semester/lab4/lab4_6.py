from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def compute_z_function(s):
    n = len(s)
    z_function = [0] * (n - 1)
    l, r = 0, 0  # Границы самого правого подстроки совпадения

    for i in range(1, n):
        if i <= r:
            # Если i находится внутри текущего подстроки совпадения,
            # используем уже вычисленные значения для i
            z_function[i - 1] = min(r - i + 1, z_function[i - l - 1])

        while i + z_function[i - 1] < n and s[z_function[i - 1]] == s[i + z_function[i - 1]]:
            z_function[i - 1] += 1

        if i + z_function[i - 1] - 1 > r:
            l, r = i, i + z_function[i - 1] - 1

    return z_function


def main():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()
    z_function = compute_z_function(s)

    with open('output.txt', 'w') as file:
        file.write(" ".join(map(str, z_function)))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
