# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def min_height(root):
            if not root:
                return 0
            
            left = min_height(root.left)
            right = min_height(root.right)
            
            # excluding null branches per problem description 
            if right == 0:
                return left + 1
            if left == 0:
                return right + 1
            
            return min(left, right) + 1
        
        return min_height(root)
