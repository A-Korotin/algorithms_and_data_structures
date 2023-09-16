from util.performance.time_measurement import get_function_execution_time_sec
from util.performance.mem_measurement import *
from util.performance.summary import *


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)
        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value(root.right)
            root.right = self._delete_recursive(root.right, root.key)
        return root

    def exists(self, key):
        return self._exists_recursive(self.root, key)

    def _exists_recursive(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        if key < root.key:
            return self._exists_recursive(root.left, key)
        return self._exists_recursive(root.right, key)

    def next(self, key):
        return self._next_recursive(self.root, key)

    def _next_recursive(self, root, key):
        if root is None:
            return "none"
        if key < root.key:
            left_result = self._next_recursive(root.left, key)
            if left_result == "none":
                return root.key
            return left_result
        return self._next_recursive(root.right, key)

    def prev(self, key):
        return self._prev_recursive(self.root, key)

    def _prev_recursive(self, root, key):
        if root is None:
            return "none"
        if key > root.key:
            right_result = self._prev_recursive(root.right, key)
            if right_result == "none":
                return root.key
            return right_result
        return self._prev_recursive(root.left, key)

    @staticmethod
    def _min_value(node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key


def main():
    bst = BinarySearchTree()

    with open("input.txt", 'r') as f_in, open('output.txt', 'w') as f_out:
        for line in f_in:
            operation, value = line.strip().split()
            value = int(value)
            if operation == "insert":
                bst.insert(value)
            elif operation == "delete":
                bst.delete(value)
            elif operation == "exists":
                f_out.write(str(bst.exists(value)).lower() + "\n")
            elif operation == "next":
                result = bst.next(value)
                f_out.write(str(result) + "\n")
            elif operation == "prev":
                result = bst.prev(value)
                f_out.write(str(result) + "\n")


if __name__ == "__main__":
    start_mem_trace()
    time, _ = get_function_execution_time_sec(main)
    mem = get_max_mem_usage_mb()
    print_time_and_mem_usage_summary(time, mem)
