# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node'):
        if root is None:
            return
        tree = []
        recurse(root, tree)
        tree.append(root.val)
        return tree
    
def recurse(node, tree):
    if node is None:
        return
    for child in node.children:
        recurse(child, tree)
        tree.append(child.val)