from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])


def union(parent, rank, x, y):
    root_x = find_parent(parent, x)
    root_y = find_parent(parent, y)

    if root_x != root_y:
        if rank[root_x] < rank[root_y]:
            root_x, root_y = root_y, root_x
        parent[root_y] = root_x
        if rank[root_x] == rank[root_y]:
            rank[root_x] += 1


def kruskal_max_distance(points, k):
    edges = []
    n = len(points)

    # Создание списка всех ребер с расстояниями
    for i in range(n):
        for j in range(i + 1, n):
            distance = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            edges.append((distance, i, j))

    # Сортировка ребер по возрастанию расстояний
    edges.sort()

    parent = list(range(n))
    rank = [0] * n
    clusters = n

    # Поиск максимального расстояния d
    for distance, u, v in edges:
        if find_parent(parent, u) != find_parent(parent, v):
            if clusters == k:  # Мы достигли нужного числа кластеров
                return distance
            union(parent, rank, u, v)
            clusters -= 1

    return 0  # Если k > n, то необходимо вернуть 0


def main():
    # Считывание данных
    with open('input.txt', 'r') as f:
        n = int(f.readline())
        points = [tuple(map(int, f.readline().split())) for _ in range(n)]
        k = int(f.readline())

    # Нахождение и вывод ответа
    max_distance = kruskal_max_distance(points, k)
    with open('output.txt', 'w') as f:
        f.write(format(max_distance, ".7f"))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
