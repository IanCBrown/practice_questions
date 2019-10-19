# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L: int, R: int) -> int:
        list_of_nodes = []
        total = 0
        list_of_nodes = inorder(root, list_of_nodes)
        for node in list_of_nodes:
            if node >= L and node <= R:
                total += node
        return total
        
              
def inorder(root, list_of_nodes):
    if root is None:
        return 
    inorder(root.left, list_of_nodes)
    list_of_nodes.append(root.val)
    inorder(root.right, list_of_nodes)
    return list_of_nodes
    
        