# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ptr = ListNode(0)
        
        while l1 and l2:
          
            if l1.val <= l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next    
            ptr = ptr.next
            
        
        while l1:
            ptr.next = l1
            l1 = l1.next
            ptr = ptr.next
            
        while l2:
            ptr.next = l2
            l2 = l2.next
            ptr = ptr.next
            
            
        return head.next 
    
    
# initialize head pointer
# while True
# compare l1 and l2
# assign head to the node with the lowest val
# increment the node that was just assigned 
