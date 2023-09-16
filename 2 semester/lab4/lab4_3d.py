def find_lexicographically_larger_name(x, y):
    chars = list(set(x).intersection(set(y)))
    child_name = ''

    if len(chars) != 0:
        chars.sort()
        chars.reverse()
        while len(chars) != 0:
            g = min(x.count(chars[0]), y.count(chars[0]))
            child_name += chars[0] * g
            for i in range(g):
                x = x[x.find(chars[0]) + 1:]
                y = y[y.find(chars[0]) + 1:]
            chars.pop(0)
    return child_name


def main():
    with open('input.txt', "r") as input_file:
        father_name = input_file.readline().strip()
        mother_name = input_file.readline().strip()

    child_name = find_lexicographically_larger_name(father_name, mother_name)

    with open("output.txt", "w") as output_file:
        output_file.write(child_name)


if __name__ == "__main__":
    main()
