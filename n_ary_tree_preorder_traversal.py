
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node'):
        tree = []
        recurse(root, tree)
        return tree
        
        
def recurse(node, tree):
    if node is None:
        return
    tree.append(node.val)
    for child in node.children:
        recurse(child, tree)
    