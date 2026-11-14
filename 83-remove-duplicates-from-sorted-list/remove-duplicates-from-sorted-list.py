# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # if head == None or head.next == None:
        #     return head
        # li = []
        # curr = head
        # while curr != None:
        #     if curr.val not in li:
        #         li.append(curr.val)
        #     curr = curr.next
        # curr = head
        # k = 0
        # # prev = curr
        # while k < len(li):
        #     prev = curr
        #     curr.val = li[k]
        #     curr = curr.next
        #     k += 1
        # prev.next = None
        # return head

        curr = head

        while curr != None and curr.next != None:
            if curr.val == curr.next.val :
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
           



                



