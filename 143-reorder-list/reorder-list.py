# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        rev_curr = slow.next
        slow.next = None
        prev = None
    
        while rev_curr != None:
            temp = rev_curr.next
            rev_curr.next = prev
            prev = rev_curr
            rev_curr = temp

        first = head
        second = prev

        while second != None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
