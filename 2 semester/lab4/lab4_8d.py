def main():
    a = [[0] * 101 for _ in range(27)]
    with open('input.txt', 'r') as file:
        s = file.readline().strip()
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            a[ord(s[i]) - ord('a') + 1][j] += 1

    t = True
    l = n

    while t and l > 1:
        l -= 1

        for i in range(n - l + 1):
            for j in range(i + 1, n - l + 1):
                v = True

                for c in range(1, 27):
                    v = v and ((a[c][i + l] - a[c][i]) == (a[c][j + l] - a[c][j]))

                if v:
                    t = False

    with open('output.txt', 'w') as file:
        file.write('0' if t else str(l))


if __name__ == "__main__":
    main()