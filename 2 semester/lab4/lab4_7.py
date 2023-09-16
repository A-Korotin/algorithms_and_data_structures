from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def hash_string(s, p, x):
    """Хеширование строки s с простым модулем p и основанием x."""
    h = 0
    for i in range(len(s) - 1, -1, -1):
        h = (h * x + ord(s[i])) % p
    return h


def precompute_hashes(text, pattern_length, p, x):
    """Предвычисление хешей для всех подстрок длины pattern_length в тексте."""
    text_length = len(text)
    h = [0] * (text_length - pattern_length + 1)
    h[-1] = hash_string(text[text_length - pattern_length:], p, x)
    y = 1
    for _ in range(pattern_length):
        y = (y * x) % p
    for i in range(text_length - pattern_length - 1, -1, -1):
        h[i] = (x * h[i + 1] + ord(text[i]) - y * ord(text[i + pattern_length])) % p
    return h


def find_longest_common_substring(s, t):
    p = 10 ** 9 + 7  # Простое модульное число
    x = 263         # Основание хеширования
    max_length = 0
    result = (0, 0, 0)  # (начальная позиция в s, начальная позиция в t, длина)

    # Двоичный поиск по длинам общих подстрок
    left, right = 0, min(len(s), len(t)) + 1
    while left < right - 1:
        length = (left + right) // 2
        s_hashes = precompute_hashes(s, length, p, x)
        t_hashes = precompute_hashes(t, length, p, x)
        found = False

        for i in range(len(s) - length + 1):
            if s_hashes[i] in t_hashes:
                j = t_hashes.index(s_hashes[i])
                if s[i:i + length] == t[j:j + length]:
                    found = True
                    break

        if found:
            max_length = length
            result = (i, j, max_length)
            left = length
        else:
            right = length

    return result


def main():
    with open('input.txt', 'r') as f_in, open('output.txt', 'w') as f_out:

        for line in f_in.readlines():
            s, t = line.strip().split()
            i, j, length = find_longest_common_substring(s, t)
            f_out.write(f"{i} {j} {length}\n")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
