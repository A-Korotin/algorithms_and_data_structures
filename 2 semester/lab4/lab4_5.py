from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def compute_prefix_function(s):
    n = len(s)
    prefix_function = [0] * n

    for i in range(1, n):
        j = prefix_function[i - 1]
        while j > 0 and s[i] != s[j]:
            j = prefix_function[j - 1]
        if s[i] == s[j]:
            j += 1
        prefix_function[i] = j

    return prefix_function


def main():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()
    prefix_function = compute_prefix_function(s)
    with open('output.txt', 'w') as file:
        file.write(" ".join(map(str, prefix_function)))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
