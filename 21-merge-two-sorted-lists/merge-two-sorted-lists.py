# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        head = ListNode()
        curr = head

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1 != None:
            curr.next = list1
        else:
            curr.next = list2

        return head.next



