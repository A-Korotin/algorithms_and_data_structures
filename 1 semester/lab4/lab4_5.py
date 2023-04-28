from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *
from typing import Any


class Stack:
    def __init__(self) -> None:
        self.__container = []
        self.__maximums = []

    def __copy_last_max(self):
        self.__maximums.append(self.__maximums[-1])

    def push(self, value) -> None:
        if len(self.__maximums) == 0:
            self.__maximums.append(value)
        else:
            if value > self.__maximums[-1]:
                self.__maximums.append(value)
            else:
                self.__copy_last_max()

        self.__container.append(value)

    def pop(self) -> Any:
        if len(self) > 0:
            self.__maximums.pop()
            return self.__container.pop()

    def __len__(self):
        return len(self.__container)

    def __repr__(self) -> str:
        return ' '.join(self.__container)

    def max(self):
        if len(self.__maximums) > 0:
            return self.__maximums[-1]


def main():
    stack = Stack()
    commands = []
    with open('io_folder/input.txt', 'r') as file:
        for _ in range(int(file.readline())):
            commands.append(file.readline().strip())

    with open('io_folder/output.txt', 'w') as file:
        for c in commands:
            command = c.split(' ')
            if command[0] == 'push':
                stack.push(int(command[-1]))
            if command[0] == 'pop':
                stack.pop()
            if command[0] == 'max':
                file.write(f'{stack.max()}\n')


if __name__ == "__main__":
    start_mem_trace()
    with open('io_folder/input.txt', 'w') as file:
        n = 4*10 ** 5
        file.write(f"{n}\n")
        for i in range(n-1000):
            file.write(f"push {i}\n")

        for i in range(1000):
            file.write("max\n")

    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)



