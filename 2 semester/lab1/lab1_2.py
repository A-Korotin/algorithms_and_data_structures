from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def main():
    with open('input.txt', 'r') as f_in:
        d = int(f_in.readline())
        m = int(f_in.readline())
        n = int(f_in.readline())
        stops = list(map(int, f_in.readline().split()))

    stops = [0] + stops + [d]  # добавляем начальную и конечную точки в список остановок
    num_refills = 0
    current_refill = 0

    with open("output.txt", 'w') as f_out:
        while current_refill <= n:
            last_refill = current_refill
            while current_refill <= n and stops[current_refill + 1] - stops[last_refill] <= m:
                current_refill += 1
            if current_refill == last_refill:
                f_out.write("-1")
                return
            if current_refill <= n:
                num_refills += 1

        f_out.write(str(num_refills))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
