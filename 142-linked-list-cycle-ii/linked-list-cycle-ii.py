# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def find_first(self,slow,fast):
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # d = {}
        # pointer = 0
        # curr = head
        # while curr != None:
        #     if curr not in d:
        #         d[curr] = pointer
        #         pointer += 1
        #         curr = curr.next
        #     else:
        #         return curr
        # return None


        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return self.find_first(head,fast)

        return None





















