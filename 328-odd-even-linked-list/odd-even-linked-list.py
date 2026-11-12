# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        stack = []
        odd = head

        while odd != None and odd.next != None:
            stack.append(odd.val)
            odd = odd.next.next
        
        if odd != None:
            stack.append(odd.val)
        
        even = head.next
        while even != None and even.next != None:
            stack.append(even.val)
            even = even.next.next
        
        if even != None:
            stack.append(even.val)

        curr = head
        k = 0

        while curr != None:
            curr.val = stack[k]
            curr = curr.next
            k += 1

        return head