from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


class Node:
    def __init__(self, key, left_child=None, right_child=None):
        self.key = key
        self.left_child = left_child
        self.right_child = right_child


def is_bst(nodes, i, min_val, max_val):
    if i == -1:
        return True
    if nodes[i].key <= min_val or nodes[i].key >= max_val:
        return False
    return is_bst(nodes, nodes[i].left_child, min_val, nodes[i].key) and is_bst(nodes, nodes[i].right_child, nodes[i].key, max_val)



def main():
    # Чтение данных из файла
    with open('input.txt', 'r') as file:
        n = int(file.readline())

        nodes = list()

        for i in range(1, n + 1):
            key, left_child, right_child = map(int, file.readline().split())
            nodes.append(Node(key, left_child - 1, right_child - 1))

    # Проверка свойства двоичного дерева поиска
    if is_bst(nodes, 0, -float("inf"), float('inf')):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)

