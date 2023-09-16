from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def find_substring_occurrences(p, t):
    occurrences = []
    p_length = len(p)
    t_length = len(t)

    for i in range(t_length - p_length + 1):
        if t[i:i + p_length] == p:
            occurrences.append(i + 1)  # Добавляем 1, так как символы нумеруются с единицы

    return occurrences


def main():
    with open("input.txt", "r") as f:
        p = f.readline().strip()
        t = f.readline().strip()

    occurrences = find_substring_occurrences(p, t)

    with open("output.txt", "w") as f:
        f.write(str(len(occurrences)) + "\n")
        f.write(" ".join(map(str, occurrences)) + "\n")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)