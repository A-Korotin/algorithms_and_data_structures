from typing import Tuple, IO


def read_input(file: IO) -> Tuple[int, int]:
    line = file.readline().split()
    a, b, *_ = map(int, line)

    return a, b


def writeln(file: IO, string: str) -> None:
    file.write(string + "\n")


if __name__ == "__main__":

    with open("io/input.txt", "r") as file:
        a, b = read_input(file)

    with open("io/output.txt", "w") as file:
        writeln(file, str(a + b))
        writeln(file, str(a + b ** 2))


