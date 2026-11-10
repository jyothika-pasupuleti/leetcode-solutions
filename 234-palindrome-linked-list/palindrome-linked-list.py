# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        curr = head
        stack = []

        while curr != None:
            stack.append(curr.val)
            curr = curr.next
        
        stack.reverse()
        # i = 0
        # j = len(stack)-1
        # while i < j:
        #     stack[i],stack[j] = stack[j],stack[i]

        
        pcurr = head
        k = 0

        while pcurr != None:
            if pcurr.val != stack[k]:
                return False
            pcurr = pcurr.next
            k += 1

        return True


        
