from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def bfs(graph, start, target):
    queue = [(start, 0)]
    visited = set()

    while queue:
        current, steps = queue.pop(0)
        visited.add(current)

        if current == target:
            return steps

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, steps + 1))

    return -1


def main():
    with open("input.txt", 'r') as f:
        m = int(f.readline())
        reactions = {}
        for _ in range(m):
            src, dest = f.readline().strip().split(" -> ")
            reactions.setdefault(src, []).append(dest)
        start = f.readline().strip()
        target = f.readline().strip()

    result = bfs(reactions, start, target)

    with open("output.txt", 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
