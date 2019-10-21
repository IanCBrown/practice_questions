# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """                               
        levels = height(root)
        sol = level_order_helper(root, levels)
        return sol     
        
def level_order_helper(root, levels):
    avgs = []
    for i in range(1,levels + 1):
        nodes = []
        l = level_order(root, i, nodes)
        avgs.append(sum(l)/len(l))
    return avgs
    
def level_order(root, level,nodes):
    if root is None:
        return
    if level == 1:
        nodes.append(root.val)
    if level > 1:
        level_order(root.left, level - 1, nodes)
        level_order(root.right, level - 1, nodes)
    return nodes

def height(root):
    if root is None:
        return 0
    left_max = height(root.left)
    right_max = height(root.right)
    return max(left_max, right_max) + 1
        