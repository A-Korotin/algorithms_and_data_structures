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
        if len(self) > 0:
            return self.__container.pop()

    def __len__(self):
        return len(self.__container)

    def __repr__(self) -> str:
        return ' '.join(self.__container)


def solve_sequence(sequence: str) -> bool:
    open_round = '('
    close_round = ')'
    open_square = '['
    close_square = ']'
    is_valid_sequence: bool = True
    stack: Stack = Stack()
    for i in sequence:
        if i in [open_square, open_round]:
            stack.push(i)
        elif i == close_square and stack.pop() != open_square:
            is_valid_sequence = False
            break
        elif i == close_round and stack.pop() != open_round:
            is_valid_sequence = False
            break

    if len(stack) > 0:
        is_valid_sequence = False

    return is_valid_sequence


def main():
    seq = []
    with open('io_folder/input.txt', 'r') as file:
        for _ in range(int(file.readline())):
            seq.append(file.readline().strip())

    with open('io_folder/output.txt', 'w') as file:
        for sequence in seq:
            file.write(f'{"YES" if solve_sequence(sequence) else "NO"}\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)

