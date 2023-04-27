from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


class HashTable:
    def __init__(self, m: int) -> None:
        self.__m = m
        self.__table = [[] for _ in range(m)]

    def __hash(self, string: str) -> int:
        return (sum(ord(el) * (263 ** i) for i, el in enumerate(string)) % 1000000007) % self.__m

    def add(self, s: str) -> None:
        h = self.__hash(s)
        if s not in self.__table[h]:
            self.__table[h].append(s)

    def delete(self, s: str) -> None:
        h = self.__hash(s)
        if s in self.__table[h]:
            self.__table[h].remove(s)

    def find(self, s: str) -> str:
        h = self.__hash(s)
        if s in self.__table[h]:
            return "yes"
        else:
            return "no"

    def check(self, i: int) -> str:
        return " ".join(self.__table[i][::-1])


def main():
    with open("io_folder/input.txt", 'r') as inp, open("io_folder/output.txt", 'w') as out:
        m = int(inp.readline())
        n = int(inp.readline())
        table = HashTable(m)
        for i in range(n):
            cmd, arg = inp.readline().split()
            if cmd == "add":
                table.add(arg)
            elif cmd == "del":
                table.delete(arg)
            elif cmd == "find":
                out.write(f'{table.find(arg)}\n')
            elif cmd == "check":
                out.write(f'{table.check(int(arg))}\n')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)







