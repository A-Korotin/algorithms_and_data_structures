from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def has_negative_cycle(graph, n):
    distances = [float('inf')] * n
    distances[0] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

    for u in range(n):
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                return 1  # Граф содержит цикл с отрицательным суммарным весом

    return 0  # Граф не содержит цикл с отрицательным суммарным весом


def main():
    with open("input.txt", 'r') as f:
        n, m = map(int, f.readline().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, weight = map(int, f.readline().split())
            graph[u - 1].append((v - 1, weight))

    result = has_negative_cycle(graph, n)

    with open("output.txt", 'w') as f:
        f.write(str(result))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)