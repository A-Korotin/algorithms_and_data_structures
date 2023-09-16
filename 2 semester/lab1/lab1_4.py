import random

from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


def main():
    with open("input.txt", 'r') as f_in:
        n = int(f_in.readline())
        segments = []
        for i in range(n):
            a, b = map(int, f_in.readline().split())
            segments.append((a, b))

    # сортируем отрезки по правым концам, а при равных правых концах - по левым концам
    segments.sort(key=lambda x: (x[1], x[0]))

    points = []
    last_point = -1
    for a, b in segments:
        if a > last_point:
            # если начало отрезка больше, чем последняя точка, добавляем точку в ответ
            points.append(b)
            last_point = b

    with open("output.txt", 'w') as f_out:
        f_out.write(f'{len(points)}\n{" ".join(map(str, points))}')


if __name__ == "__main__":
    n = 1
    with open("input.txt", 'w') as f_in:
        f_in.write(f'{n}\n')
        for _ in range(n):
            a = random.randint(0, 1)
            b = a
            while b == a:
                b = random.randint(0, 2)

            f_in.write(" ".join(map(str, sorted([a, b]))) + "\n")

    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)