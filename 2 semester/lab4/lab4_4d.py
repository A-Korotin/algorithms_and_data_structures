def solve(s):
    l1 = l2 = len(s)
    for i in range(1, l2 + 1):
        if l2 % i == 0:
            c = l2 // i
            if s[:i] * c == s:
                l1 = i
                break
            elif s[:c] * i == s:
                l1 = c

    return len(s) // l1


def main():
    with open('input.txt', 'r') as f:
        s = f.readline().strip()

    with open('output.txt', 'w') as f:
        f.write(str(solve(s)))


if __name__ == "__main__":
    main()
