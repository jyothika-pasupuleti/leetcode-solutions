# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # curr = head
        # stack = []

        # while curr != None:
        #     stack.append(curr.val)
        #     curr = curr.next
        
        # stack.reverse()
        # # i = 0
        # # j = len(stack)-1
        # # while i < j:
        # #     stack[i],stack[j] = stack[j],stack[i]
   
        # curr = head
        # k = 0

        # while curr != None:
        #     if curr.val != stack[k]:
        #         return False
        #     curr = curr.next
        #     k += 1

        # return True

        def rev_ll(curr):
            prev = None
            while curr != None:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev
    
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next


        mid = rev_ll(slow)
        curr = head

        while mid != None:
            if curr.val != mid.val:
                return False
            mid = mid.next
            curr = curr.next
                
        return True


        
