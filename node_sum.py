class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def sum_of_nodes(root):
    if root is None:
        return 0
    return root.data + sum_of_nodes(root.left) + sum_of_nodes(root.right)


# Example usage
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Calculate the sum of nodes
sum_of_all_nodes = sum_of_nodes(root)
print("Sum of all nodes:", sum_of_all_nodes)
