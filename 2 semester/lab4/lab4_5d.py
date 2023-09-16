def compute_prefix_function(pattern):
    m = len(pattern)
    prefix_function = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            prefix_function[i] = length
            i += 1
        else:
            if length != 0:
                length = prefix_function[length - 1]
            else:
                prefix_function[i] = 0
                i += 1

    return prefix_function


def find_occurrences(s, t):
    n = len(s)
    m = len(t)
    prefix_function = compute_prefix_function(t)

    occurrences = []
    i = j = 0

    while i < n:
        if t[j] == s[i]:
            i += 1
            j += 1

            if j == m:
                occurrences.append(i - j)
                j = prefix_function[j - 1]
        else:
            if j != 0:
                j = prefix_function[j - 1]
            else:
                i += 1

    return occurrences


def main():
    with open('input.txt', 'r') as file:
        s = file.readline().strip()
        t = file.readline().strip()

    answer = find_occurrences(s, t)

    with open('output.txt', 'w') as file:
        file.write(" ".join(map(str, answer)))


if __name__ == "__main__":
    main()

