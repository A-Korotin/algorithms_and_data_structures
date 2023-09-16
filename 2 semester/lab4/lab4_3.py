# from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
# from util.performance.summary import print_time_and_mem_usage_summary
# from util.performance.time_measurement import get_function_execution_time_sec
#
#
# def rabin_karp(pattern, text):
#     prime = 101  # Простое число для хеширования
#     p_len = len(pattern)
#     t_len = len(text)
#     p_hash = sum(ord(pattern[i]) * (prime ** i) for i in range(p_len))
#     t_hash = sum(ord(text[i]) * (prime ** i) for i in range(p_len))
#     occurrences = []
#
#     for i in range(t_len - p_len + 1):
#         if p_hash == t_hash:
#             if pattern == text[i:i + p_len]:
#                 occurrences.append(i + 1)
#
#         if i + p_len < t_len:
#             t_hash = (t_hash - ord(text[i])) // prime + ord(text[i + p_len]) * (prime ** (p_len - 1))
#
#     return occurrences
#
#
# def main():
#     # Чтение входных данных из файла
#     with open("input.txt", "r") as input_file:
#         pattern = input_file.readline().strip()
#         text = input_file.readline().strip()
#
#     # Поиск вхождений
#     occurrences = rabin_karp(pattern, text)
#
#     # Запись результата в выходной файл
#     with open("output.txt", "w") as output_file:
#         output_file.write(str(len(occurrences)) + "\n")
#         output_file.write(" ".join(map(str, occurrences)))
#
#
# if __name__ == "__main__":
#     start_mem_trace()
#     time, _ = get_function_execution_time_sec(main)
#     mem = get_max_mem_usage_mb()
#     print_time_and_mem_usage_summary(time, mem)
import math

matrix = []
with open("D:\Downloads\Telegram Desktop\in-22.txt", 'r') as file:
    N, M, K = map(int, file.readline().split())
    for _ in range(N):
        matrix.append(list(map(int, file.readline().split())))

    for _ in range(K):
        i, j, val = map(int, file.readline().split())
        matrix[i][j] = val

s = 0

for row in matrix:
    s += sum(row)

print(s)




