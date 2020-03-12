# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        left = deque()
        right = deque()
        
        while l1 is not None:
            left.appendleft(str(l1.val))
            l1 = l1.next
        
        while l2 is not None:
            right.appendleft(str(l2.val))
            l2 = l2.next
        
        print(list(left))
        l = int("".join(list(left)))
        r = int("".join(list(right)))
        ret = l + r
        
        ret = [int(i) for i in reversed(str(ret))]
        head = ListNode(ret[0])
        curr = head
        print(ret)
        for i in range(1, len(ret)):
            curr.next = ListNode(ret[i])
            curr = curr.next
            
        return head
