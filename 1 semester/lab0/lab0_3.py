from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import get_max_mem_usage_mb, start_mem_trace
from util.performance.summary import print_time_and_mem_usage_summary


def calc_fib_last_digit(n: int) -> int:
    if n <= 1:
        return n

    f2 = 0
    f1 = 1
    current = 1

    for _ in range(2, n + 1):
        current = (f1 + f2) % 10
        f2 = f1
        f1 = current

    return current


if __name__ == "__main__":
    start_mem_trace()

    with open("io/input.txt", "r") as file:
        n = int(file.readline())

    time, answer = get_function_execution_time_sec(calc_fib_last_digit, n)

    max_mem = get_max_mem_usage_mb()

    with open("io/output.txt", "w") as file:
        file.write(str(answer))

    print_time_and_mem_usage_summary(time, max_mem)
