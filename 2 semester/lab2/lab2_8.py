from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def main():
    tree = []
    children = []
    with open("input.txt", 'r') as file:
        n = int(file.readline())
        for _ in range(n):
            key, left, right = map(int, file.readline().split())
            tree.append(Node(key))
            children.append([left, right])
    for i, (left, right) in enumerate(children):
        node = tree[i]
        node.left = tree[left - 1] if left != 0 else None
        node.right = tree[right - 1] if right != 0 else None

    with open("output.txt", 'w') as file:
        file.write(str(height(tree[0])))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
