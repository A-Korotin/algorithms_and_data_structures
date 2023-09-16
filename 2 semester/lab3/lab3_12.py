from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def is_incorrect_path(graph, path):
    room = 0
    is_incorrect = False
    for i in range(len(path)):
        c = path[i] - 1
        if c not in graph[room].keys():
            is_incorrect = True
            break
        p2 = graph[room][c]
        if p2 is not None:
            room = p2
        else:
            is_incorrect = True
            break
    return is_incorrect, room + 1


def main():
    with open("input.txt", 'r') as file:
        n, m = map(int, file.readline().split())
        graph = [{} for _ in range(n)]
        for _ in range(m):
            f, s, c = map(int, file.readline().split())
            graph[f - 1][c - 1] = s - 1
            graph[s - 1][c - 1] = f - 1
        file.readline()  # k
        path = list(map(int, file.readline().split()))

    incorrect, p = is_incorrect_path(graph, path)
    with open('output.txt', 'w') as file:
        file.write("INCORRECT" if incorrect else str(p))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
