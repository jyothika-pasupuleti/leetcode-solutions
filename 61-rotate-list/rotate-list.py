# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        if head == None or head.next == None:
            return head
        length = 1
        tail = head

        while tail.next != None:
            tail = tail.next
            length += 1

        if k%length == 0:
            return head

        tail.next = head

        k = k % length
        res = length - k

        curr = head

        while res != 1:
            curr = curr.next
            res -= 1

        head = curr.next
        curr.next = None

        return head
