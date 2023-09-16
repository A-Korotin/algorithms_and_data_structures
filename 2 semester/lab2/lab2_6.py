from util.performance.mem_measurement import start_mem_trace, get_max_mem_usage_mb
from util.performance.summary import print_time_and_mem_usage_summary
from util.performance.time_measurement import get_function_execution_time_sec


class Node:
   def __init__(self, key):
       self.key = key
       self.left = None
       self.right = None


def tree_check(node, min_val, max_val):
   if node is None:
       return True
   if node.key < min_val or node.key > max_val:
       return False
   return tree_check(node.left, min_val, node.key) and tree_check(node.right, node.key, max_val)


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
       node.left = tree[left] if left != -1 else None
       node.right = tree[right] if right != -1 else None

   with open("output.txt", 'w') as file:
       file.write("CORRECT" if tree_check(tree[0], -(2**31) - 1, 2**31 + 1) else "INCORRECT")


if __name__ == "__main__":
   start_mem_trace()
   time, _ = get_function_execution_time_sec(main)
   mem = get_max_mem_usage_mb()
   print_time_and_mem_usage_summary(time, mem)
