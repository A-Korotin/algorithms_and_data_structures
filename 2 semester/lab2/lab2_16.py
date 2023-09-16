from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1  # Количество узлов в поддереве с корнем в данном узле


def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)

    root.count += 1
    return root


def kth_max(root, k):
    if root is None:
        return None

    right_count = 1 + (root.right.count if root.right else 0)

    if right_count == k:
        return root.key
    elif right_count < k:
        return kth_max(root.left, k - right_count)
    else:
        return kth_max(root.right, k)


def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        min_key = find_min_key(root.right)
        root.key = min_key
        root.right = delete(root.right, min_key)

    root.count -= 1
    return root


def find_min_key(root):
    while root.left:
        root = root.left
    return root.key


def main():

    # Чтение входных данных
    with open("input.txt", "r") as input_file:
        n = int(input_file.readline())
        commands = [list(map(int, line.split())) for line in input_file]

    root = None
    output = []

    # Обработка команд
    for command in commands:
        if command[0] == 1:
            root = insert(root, command[1])
        elif command[0] == 0:
            k_max = kth_max(root, command[1])
            output.append(k_max)
        elif command[0] == -1:
            root = delete(root, command[1])

    # запись данных в файл
    with open("output.txt", "w") as output_file:
        output_file.write("\n".join(map(str, output)))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
