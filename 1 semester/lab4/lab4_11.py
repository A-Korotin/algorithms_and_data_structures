from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *

from collections import deque


def solve_queue(queue, m):
    dq = deque(queue)
    for _ in range(m):
        if len(dq) == 0:
            return -1
        visitor = dq.popleft() - 1
        if visitor > 0:
            dq.append(visitor)

    return dq


def main():
    m: int
    q: list
    with open('io_folder/input.txt', 'r') as file:
        _, m = map(int, file.readline().strip().split())
        q = list(map(int, file.readline().strip().split(' ')))

    with open('io_folder/output.txt', 'w') as file:
        ans = solve_queue(q, m)
        if ans == -1:
            file.write("-1\n")
            return

        file.write(f'{len(ans)}\n{" ".join(str(ans.popleft()) for _ in range(len(ans)))}')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)



