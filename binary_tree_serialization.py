

class Node:
    def __init__(self, data_in):
        self.data = data_in
        self.left = None
        self.right = None

arr = [] 

def serialize(root):
    if root is not None:
        arr.append(root.value)
        serialize(root.left)
        serialize(root.right)
    else:
        arr.append(root)


arr = iter(arr)
def deserialize(arr):
    root = next(arr)
    if root is not None:
        root = Node(root)
        deserialize(root.left)
        deserialize(root.right)
    else:
        return root



    