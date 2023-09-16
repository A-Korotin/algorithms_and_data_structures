from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def kosaraju(edges, n):
    graph = [[] for _ in range(n)]
    transposed = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        transposed[v].append(u)

    def dfs(node, graph, visited, stack):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        stack.append(node)

    def dfs_transposed(node, transposed, visited):
        visited[node] = True
        for neighbor in transposed[node]:
            if not visited[neighbor]:
                dfs_transposed(neighbor, transposed, visited)

    visited = [False] * n
    stack = []
    for node in range(n):
        if not visited[node]:
            dfs(node, graph, visited, stack)

    visited = [False] * n
    num_components = 0
    while stack:
        node = stack.pop()
        if not visited[node]:
            dfs_transposed(node, transposed, visited)
            num_components += 1

    return num_components


def main():
    edges = []
    with open("input.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        for line in file.readlines():
            a, b = map(int, line.split())
            edges.append((a - 1, b - 1))

    num_strong_components = kosaraju(edges, n)

    with open("output.txt", 'w') as file:
        file.write(str(num_strong_components))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
