import sys
import threading

# This class will help us to create a node
class Node:
    def __init__(self):
        self.children = []

# This function will help us to create a tree
def create_tree(n, parents):
    nodes = [Node() for _ in range(n)]
    root = 0
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].children.append(nodes[child_index])
    return nodes[root]

# This function will help us to compute the height of the tree
def compute_height(node):
    if not node.children:
        return 1
    else:
        return 1 + max(compute_height(child) for child in node.children)

# This function will help us to read input data and run the solution
def main():
    # implement input form keyboard and from files
    input_type = input("Input from File or Keyboard? (F/K): ")
    if input_type.upper() == "F":
        # let user input file name to use, don't allow file names with letter a
        file_name = input("Enter file name (should not contain letter 'a'): ")
        while 'a' in file_name:
            file_name = input("Enter file name (should not contain letter 'a'): ")
        with open(file_name) as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    elif input_type.upper() == "K":
        # input number of elements
        # input values in one variable, separate with space, split these values in an array
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        print("Invalid input type. Please enter F for file or K for keyboard input.")
        return
    # call the function and output it's result
    tree = create_tree(n, parents)
    print(compute_height(tree))

# Increase the recursion limit and the stack size
sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

# Run the solution in a new thread
threading.Thread(target=main).start()
