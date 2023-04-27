from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


class Set:
    def __init__(self):
        self.data = {}

    def add(self, x):
        self.data[x] = True

    def remove(self, x):
        if x in self.data:
            del self.data[x]

    def exists(self, x):
        return 'Y' if x in self.data else 'N'


def main():
    set = Set()
    with open('io_folder/input.txt', 'r') as input_file, open("io_folder/output.txt", 'w') as out:
        n = int(input_file.readline())
        for i in range(n):
            line = input_file.readline().strip()
            op, x = line.split()
            x = int(x)
            if op == 'A':
                set.add(x)
            elif op == 'D':
                set.remove(x)
            elif op == '?':
                out.write(f'{set.exists(x)}\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)

