
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_valid(root, min_left, max_right):
    if root is None:
        return True

    if root.data < min_left or root.data > max_right:
        return False
    
    if root.left.data is not None and root.left.data > min_left:
        is_valid(root.left, min_left, root.left.data - 1)
    if root.right.data is not None and root.right.data < max_right:
        is_valid(root.right, root.right.data, max_right + 1)




root = Node(10)
root.left = Node(5)
root.right = Node(15)
min_left = float('-inf')
max_right = float('inf')

