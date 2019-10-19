# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root, L: int, R: int) -> int:          
        def dfs(root):
            if root:
                if root.val >= L and root.val <= R:
                    self.total += root.val
                # too small
                if root.val < R:
                    dfs(root.right)
                # too big
                if root.val > L:
                    dfs(root.left)
        
        self.total = 0 
        dfs(root)
        return self.total 