# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return fast_pointer(head)
    
def with_set(head):
    visited = set()
        
    curr = head

    while curr is not None:
        if curr in visited:
            return True
        else:
            visited.add(curr)
        curr = curr.next

    return False
    

def fast_pointer(head):
    if head is None:
        return False
    
    slow = head 
    fast = head
    
    while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
    return False
        
