from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec
from collections import deque


def is_recursive(graph, procedure):
    queue = deque()
    visited = set()
    pending = set()
    queue.append(procedure)
    pending.add(procedure)
    while len(queue) > 0:
        c = queue.popleft()
        pending.remove(c)
        visited.add(c)
        for v in graph[c]:
            if v == procedure:
                return True
            if v not in visited and v not in pending:
                queue.append(v)
                pending.add(v)
    return False


def main():
    with open("input.txt", 'r') as f:
        N = int(f.readline())
        graph, res, pcs = {}, [], []
        for _ in range(N):
            procedure = f.readline().strip()
            pcs.append(procedure)
            n = int(f.readline())
            calls = [f.readline().strip() for _ in range(n)]
            graph[procedure] = calls
            f.readline()

    with open("output.txt", 'w') as f:
        for p in pcs:
            f.write("YES\n" if is_recursive(graph, p) else "NO\n")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
