# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = ListNode(0)

        curr = head
        carry = 0
        while l1 != None and l2 != None:
            s = l1.val + l2.val + carry
            rem = s % 10
            curr.next = ListNode(rem)
            carry = s // 10
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        
        while l1 != None:
            s = l1.val + carry
            rem = s % 10
            curr.next = ListNode(rem)
            carry = s // 10
            curr = curr.next
            l1 = l1.next
            

        while l2 != None:
            s = l2.val + carry
            rem = s % 10
            curr.next = ListNode(rem)
            carry = s // 10
            curr = curr.next
            l2 = l2.next

        if carry == 1:
            curr.next = ListNode(carry)

        return head.next

