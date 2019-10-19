# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstToGst(self, root):
        list_of_nodes = []
        h = height(root)
        list_of_nodes = level_order(root, h)
        
        nums = [x for x in list_of_nodes if x != None]
        sums = get_max_sums(nums)
        ret_list = []
  
        for node in list_of_nodes:
            if node in sums:
                ret_list.append(sums[node])
            else:
                ret_list.append('null')
                
        print(ret_list)
        return rebuild(ret_list, ret_list[0], 0, len(ret_list))
        
def rebuild(list_of_nodes, root, index, length):
    if index < length:
        root = TreeNode(list_of_nodes[index])
        root.left = rebuild(list_of_nodes, root.left, 2*index + 1, length)
        root.right = rebuild(list_of_nodes, root.right, 2*index + 2, length)
    return root
            
def get_max_sums(nums):
    sums = {}
    nums.sort()
    for i in range(len(nums)):
        sums[nums[i]] = sum(nums[i:])
    return sums
    
def level_order(root, height):
    list_of_nodes = []
    for i in range(height + 1):
        level_order_helper(root, list_of_nodes, i)
    return list_of_nodes
        
def level_order_helper(root, list_of_nodes, level):
    if root is None:
        list_of_nodes.append(None)
        return
    if level == 1:
        list_of_nodes.append(root.val)
    if level > 1:
        level_order_helper(root.left, list_of_nodes, level - 1)
        level_order_helper(root.right, list_of_nodes, level - 1)

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1
        