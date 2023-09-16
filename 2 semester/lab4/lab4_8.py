from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def find_approximate_occurrences(k, t, p):
    n = len(t)
    m = len(p)
    occurrences = []

    for i in range(n - m + 1):
        mismatch_count = 0
        for j in range(m):
            if p[j] != t[i + j]:
                mismatch_count += 1
                if mismatch_count > k:
                    break

        if mismatch_count <= k:
            occurrences.append(i)

    return occurrences


def main():
    # Чтение входных данных из файла
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    results = []

    # Обработка каждой тройки (k, t, p)
    for line in lines:
        k, t, p = line.strip().split()
        k = int(k)
        occurrences = find_approximate_occurrences(k, t, p)
        results.append((len(occurrences), occurrences))

    # Запись результата в выходной файл
    with open("output.txt", "w") as output_file:
        for l, occurrences in results:
            output_file.write(str(l) + "\n")
            output_file.write(" ".join(map(str, occurrences)))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)