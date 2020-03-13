"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        
        visited = {}
        
        def traverse(head):
            if head is None:
                return None
            
            if head in visited:
                new_node = visited[head]
                return new_node
            else:
                new_node = Node(head.val)
                visited[head] = new_node
                new_node.next = traverse(head.next)
                new_node.random = traverse(head.random)
                return new_node 
        
        return traverse(head)
                
        
                
