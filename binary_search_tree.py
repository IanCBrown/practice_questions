 
 # binary search tree implementation
 # Inspired by Cracking the Coding Interview
class Node:
    def __init__(self, data_in):
        self.data = data_in
        self.left = None
        self.right = None


def insert_recursive(root, node):
    if root is None:
        root = node 
    else:
        if node.data < root.data:
            if root.left is None:
                root.left = node
            else:
                insert_recursive(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                insert_recursive(root.right, node)
    

def insert_iterative(root, node):
    return 


def search_iterative(root, data_in):
    while True:
        if root.data == data_in:
            return root
        # explore left tree
        if data_in < root.data:
            root = root.left
        # explore right tree
        root = root.right
        

def search_recursive(root, data_in):
    # base case
    if root.data == data_in:
        return root
    
    # explore left tree
    if data_in < root.data:
        return(search_recursive(root.left, data_in))
    
    # explore right tree
    return(search_recursive(root.right, data_in))


def inorder(node):
    # recurse until node is None
    if node:
        inorder(node.left)
        visit(node)
        inorder(node.right)

def preorder(node):
    # recurse until node is None
    if node:
        visit(node)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    # recurse until node is None
    if node:
        postorder(node.left)
        postorder(node.right)
        visit(node)

def visit(node):
    print(node.data)


def main():
    root = Node(3)
    insert_recursive(root, Node(2))
    insert_recursive(root, Node(1))
    insert_recursive(root, Node(4))
    insert_recursive(root, Node(5))
    inorder(root)


if __name__ == "__main__":
    main()

