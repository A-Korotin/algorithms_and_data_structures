from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


def count_palindrome_ways(line):
    palindrome_ways = 0
    first, last = ord('a'), ord('z')
    full, left = [], []
    for i in range(first, last + 1):
        full.append(0)
        left.append(0)
    for character in line:
        numeric_val = ord(character)
        full[numeric_val - first] += 1
    for character in line:
        numeric_val = ord(character) - first
        left[numeric_val] += 1
        for i in range(len(full)):
            if i == numeric_val:
                right = full[i] - left[i]
                cur_left = left[i] - 1
                palindrome_ways += cur_left * right
            else:
                right = full[i] - left[i]
                palindrome_ways += left[i] * right
    return palindrome_ways


def main():
    with open("input.txt", 'r') as file:
        message = file.readline().strip().replace(" ", "")  # Читаем послание

    result = count_palindrome_ways(message)

    with open("output.txt", 'w') as file:
        file.write(str(result))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
