from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def balance(self, node):
        if node is None:
            return node
        if self.balance_factor(node) > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if self.balance_factor(node) < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        self.update_height(node)
        return self.balance(node)

    def exists(self, key):
        return self._exists(self.root, key)

    def _exists(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._exists(node.left, key)
        return self._exists(node.right, key)

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_left_subtree = self.find_min(node.right)
            node.key = min_left_subtree.key
            node.right = self._delete(node.right, min_left_subtree.key)
        self.update_height(node)
        return self.balance(node)

    def next(self, key):
        return self._next(self.root, key)

    def _next(self, node, key):
        if node is None:
            return "none"
        if key < node.key:
            result = self._next(node.left, key)
            if result == "none" or int(result) > node.key:
                return str(node.key)
            return result
        return self._next(node.right, key)

    def prev(self, key):
        return self._prev(self.root, key)

    def _prev(self, node, key):
        if node is None:
            return "none"
        if key > node.key:
            result = self._prev(node.right, key)
            if result == "none" or int(result) < node.key:
                return str(node.key)
            return result
        return self._prev(node.left, key)


def main():
    tree = AVLTree()

    with open("input.txt", "r") as input_file:
        results = []

        for line in input_file.readlines():
            command, key = line.split()
            key = int(key)

            if command == "insert":
                tree.insert(key)
            elif command == "delete":
                tree.delete(key)
            elif command == "exists":
                results.append(str(tree.exists(key)).lower())
            elif command == "next":
                results.append(tree.next(key))
            elif command == "prev":
                results.append(tree.prev(key))

    with open("output.txt", "w") as output_file:
        output_file.write("\n".join(results))


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
