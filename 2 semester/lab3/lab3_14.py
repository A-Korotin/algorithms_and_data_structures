def main():
    with open('input.txt', 'r') as file:
        N = int(file.readline())
        D, V = map(int, file.readline().split())
        busses = [[] for _ in range(N + 1)]
        R = int(file.readline())
        for i in range(R):
            start, start_time, finish, finish_time = map(int, file.readline().split())
            busses[start].append((start_time, finish, finish_time))
    INF = float('inf')
    time = [INF] * (N + 1)
    time[D] = 0
    visited = [False] * (N + 1)
    while True:
        min_time = INF
        for i in range(1, N + 1):
            if not visited[i] and time[i] < min_time:
                min_time = time[i]
                min_village = i
        if min_time == INF:
            break
        start = min_village
        visited[start] = True
        for start_time, finish, finish_time in busses[start]:
            if time[start] <= start_time and finish_time < time[finish]:
                time[finish] = finish_time

    with open('output.txt', 'w') as file:
        file.write("-1" if time[V] == INF else str(time[V]))


if __name__ == '__main__':
    main()
