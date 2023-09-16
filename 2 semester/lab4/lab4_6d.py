def find_cyclic_shift(s1, s2):
    if len(s1) != len(s2):
        return -1
    if s1 == s2:
        return 0

    res = 0

    for i in range(len(s1)):
        shift = s1[len(s1) - i - 1:len(s1)] + s1[0:len(s1) - i - 1]
        if shift == s2:
            res += 1
            break
        res += 1
    if res == len(s1):
        res = -1

    return res


def main():
    with open('input.txt', 'r') as file:
        s1 = file.readline().strip()
        s2 = file.readline().strip()

    answer = find_cyclic_shift(s1, s2)

    with open('output.txt', 'w') as file:
        file.write(str(answer))


if __name__ == "__main__":
    main()