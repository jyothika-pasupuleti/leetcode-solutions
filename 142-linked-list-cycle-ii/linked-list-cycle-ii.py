# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        pointer = 0
        curr = head
        while curr != None:
            if curr not in d:
                d[curr] = pointer
                pointer += 1
                curr = curr.next
            else:
                return curr
        return None