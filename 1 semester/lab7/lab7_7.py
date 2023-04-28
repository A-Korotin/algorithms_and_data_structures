from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *

import re


def main():
    with open("io_folder/input.txt") as f:
        pattern = f.readline().strip()
        s = f.readline().strip()

    # замена символов ? и * на соответствующие регулярные выражения
    pattern = pattern.replace('?', '.').replace('*', '.*')

    with open('io_folder/output.txt', 'w') as file:
        if re.match(pattern, s):
            file.write("YES")
        else:
            file.write("NO")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)