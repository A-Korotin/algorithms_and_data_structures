from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *
import heapq


class Heap:
    def __init__(self):
        self.__heap = []
        self.__indexes = {}

    def add(self, x):
        heapq.heappush(self.__heap, x)
        index = len(self.__heap) - 1
        self.__indexes[id(x)] = index

    def extract_min(self):
        if self.__heap:
            min_element = heapq.heappop(self.__heap)
            del self.__indexes[id(min_element)]
            return min_element
        else:
            return "*"

    def decrease(self, x, y):

        self.__heap.pop(x)
        heapq.heappush(self.__heap, y)
        new_index = len(self.__heap) - 1
        self.__indexes[id(y)] = new_index


def main():
    with open('io_folder/input.txt', 'r') as f, open("io_folder/output.txt", 'w') as out:
        n = int(f.readline())
        heap = Heap()

        for i in range(1, n + 1):
            operation = f.readline().split()
            if operation[0] == 'A':
                x = int(operation[1])
                heap.add(x)
            elif operation[0] == 'X':
                out.write(f'{heap.extract_min()}\n')
            elif operation[0] == 'D':
                x = int(operation[1]) - 1
                y = int(operation[2])
                heap.decrease(x, y)


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
