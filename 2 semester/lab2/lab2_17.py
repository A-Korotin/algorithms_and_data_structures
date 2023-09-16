from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec
from collections import OrderedDict

M: int = 1000000001


class CustomSet:
    def __init__(self):
        self.data = OrderedDict()
        self.x = 0

    def add(self, i):
        new_i = (i + self.x) % M
        self.data[new_i] = True

    def delete(self, i):
        new_i = (i + self.x) % M
        if new_i in self.data:
            del self.data[new_i]

    def find(self, i):
        new_i = (i + self.x) % M
        if new_i in self.data:
            return "Found"
        else:
            return "Not found"

    def sum(self, l, r):
        new_l = (l + self.x) % M
        new_r = (r + self.x) % M
        if new_l <= new_r:
            total = sum(i if self.data.get(i, 0) else 0 for i in range(new_l, new_r + 1))
        else:
            total = sum(i if self.data.get(i, 0) else 0 for i in range(new_l, M)) + sum(i if
                self.data.get(i, 0) else 0 for i in range(new_r + 1))
        self.x = total
        return total


def main():
    # Чтение входных данных
    with open("input.txt", "r") as input_file:
        n = int(input_file.readline())
        queries = [input_file.readline().split() for _ in range(n)]

    # Решение и запись результатов в выходной файл
    custom_set = CustomSet()
    results = []
    for query in queries:
        operation = query[0]
        if operation == '+':
            custom_set.add(int(query[1]))
        elif operation == '-':
            custom_set.delete(int(query[1]))
        elif operation == '?':
            results.append(custom_set.find(int(query[1])))
        elif operation == 's':
            results.append(str(custom_set.sum(int(query[1]), int(query[2]))))

    with open("output.txt", "w") as output_file:
        output_file.write("\n".join(results))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
