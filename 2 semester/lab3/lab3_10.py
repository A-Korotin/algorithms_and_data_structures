from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def shortest_paths(graph, n, s):
    INF = float('inf')
    distances = [INF] * n
    distances[s] = 0

    for _ in range(n - 1):
        for u, v, w in graph:
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Проверка наличия отрицательных циклов
    for u, v, w in graph:
        if distances[u] + w < distances[v]:
            distances[v] = float('-inf')

    return distances


def main():
    with open('input.txt', 'r') as f:
        n, m = map(int, f.readline().split())
        graph = []
        for _ in range(m):
            u, v, w = map(int, f.readline().split())
            graph.append((u - 1, v - 1, w))

        s = int(f.readline())

    distances = shortest_paths(graph, n, s - 1)

    with open('output.txt', 'w') as f:
        for d in distances:
            if d == float('inf'):
                f.write('*\n')
            elif d == float('-inf'):
                f.write('-\n')
            else:
                f.write(str(d) + '\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
