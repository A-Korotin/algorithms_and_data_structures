def is_weakly_connected(graph, K):
    # Создаем матрицу смежности для графа
    adj_matrix = [[0] * (N + 1) for _ in range(N + 1)]
    for u, v in graph:
        adj_matrix[u][v] = 1

    # Вычисляем степени вершин
    degrees = [sum(adj_matrix[i]) for i in range(N + 1)]

    # Используем алгоритм Флойда-Уоршелла для поиска кратчайших путей
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                adj_matrix[i][j] = min(adj_matrix[i][j], adj_matrix[i][k] + adj_matrix[k][j])

    # Проверяем, можно ли доехать от каждой вершины до любой другой
    for u in range(1, N + 1):
        for v in range(1, N + 1):
            if adj_matrix[u][v] > K and degrees[u] > 0 and degrees[v] > 0:
                return False
    return True


def find_min_K(graph):
    left, right = 0, N - 1
    result = None

    while left <= right:
        mid = (left + right) // 2
        if is_weakly_connected(graph, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


# Считываем данные
with open('input.txt', 'r') as f:
    N, M = map(int, f.readline().split())
    graph = [tuple(map(int, f.readline().split())) for _ in range(M)]

# Находим и выводим ответ
min_K = find_min_K(graph)
with open('output.txt', 'w') as f:
    f.write(str(min_K))
