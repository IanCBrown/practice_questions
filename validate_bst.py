# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        low = float('-inf')
        high = float('inf')
        
        def validate(root, low, high):
            if root is None:
                return True
            
            if root.val > high or root.val < low:
                return False
            
            return validate(root.left, low, root.val - 1) and validate(root.right, root.val + 1, high)
        
        return validate(root, low, high)
