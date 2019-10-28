# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head) -> bool:
        # find length 
        # run through have of list 
        # check if second half matches 
        if head is None or head.next is None:
            return True
        l = length(head)
        print(l)
        mid = l // 2
        i = 0 
        
        stack = []
        while i < mid:
            stack.append(head.val)
            head = head.next 
            i += 1
        
        print(stack)
        while i < l:
            if stack[-1] == head.val:
                stack.pop()
            head = head.next
            i += 1

        return len(stack) == 0
        

        
def length(head):
    l = 0 
    while head:
        l += 1
        head = head.next
    return l 


    