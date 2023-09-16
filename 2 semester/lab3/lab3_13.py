import heapq


def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()

    while heap:
        cost, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        if node == end:
            return cost

        for neighbor, departure, destination, arrival in graph[node]:
            if departure >= cost:
                heapq.heappush(heap, (arrival, destination))

    return -1


def main():
    with open("input.txt", 'r') as f:
        N = int(f.readline())
        d, v, R = map(int, f.readline().split())
        graph = {i: [] for i in range(1, N + 1)}

        for _ in range(R):
            dep, dep_time, arr, arr_time = map(int, f.readline().split())
            graph[dep].append((dep_time, dep, arr, arr_time))

    min_time = dijkstra(graph, d, v)

    with open("output.txt", 'w') as f:
        f.write(str(min_time))


if __name__ == '__main__':
    main()
