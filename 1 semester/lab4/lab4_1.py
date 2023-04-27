from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.__container = []

    def push(self, value) -> None:
        self.__container.append(value)

    def pop(self) -> Any:
        return self.__container.pop()


def main():
    stack = Stack()
    ops = []
    with open("io_folder/input.txt", 'r') as file:
        n = int(file.readline())
        for _ in range(n):
            line = file.readline()
            ops.append(line.split(' '))

    with open('io_folder/output.txt', 'w') as file:
        for op in ops:
            res: Any = None
            if op[0].strip() == '-':
                res = stack.pop()
            else:
                res = stack.push(op[-1])

            if res is not None:
                file.write(res.strip() + '\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)