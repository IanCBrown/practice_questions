# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# https://leetcode.com/problems/inorder-successor-in-bst/submissions/

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        
        def inorder_succ(root, p):
            if root is None:
                return
            
            if p.right is not None:
                return min_value(p.right)
            
            succ = None
            while root:
                if p.val > root.val:
                    root = root.right
                elif p.val < root.val:
                    succ = root
                    root = root.left
                else:
                    return succ
        
        return inorder_succ(root,p)
    
    
    
def min_value(root):
    if root.left is None:
        return root
    
    return min_value(root.left)
