# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        arr = []
        for i in range(len(lists)):
            curr = lists[i]
            while curr != None:
                arr.append(curr.val)
                curr = curr.next
        
        arr.sort()

        if len(arr) == 0:
            return None

        head = ListNode(arr[0])
        curr = head

        for i in range(1,len(arr)):
            curr.next = ListNode(arr[i])
            curr = curr.next

        return head