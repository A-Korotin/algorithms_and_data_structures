def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi


def find_repeating_substring_length(s):
    pi = compute_prefix_function(s)
    return len(s) - pi[-1]


def main():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()

    answer = find_repeating_substring_length(s)

    with open('output.txt', 'w') as file:
        file.write(str(answer))


if __name__ == "__main__":
    main()