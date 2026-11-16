# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        length = 0
        curr = head

        while curr != None:
            length += 1
            curr = curr.next
        
        if length == n:
            return head.next

        res = length - n
        curr = head
        # while curr != None:
        #     if res == 1:
        #         break
        #     else:
        #         res -= 1
        #         curr = curr.next


        while res != 1:
            res -= 1
            curr = curr.next
            
        
        curr.next = curr.next.next
        return head