# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def merge(self,l1,l2):
    #     res = ListNode(-1)
    #     curr = res

    #     while l1 != None and l2 != None:
    #         if l1.val < l2.val:
    #             curr.next = l1
    #             l1 = l1.next
    #         else:
    #             curr.next = l2
    #             l2 = l2.next

    #         curr = curr.next

    #     if l1 != None:
    #         curr.next = l1
    #     else:
    #         curr.next = l2
    #     return res.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        # arr = []
        # for i in range(len(lists)):
        #     curr = lists[i]
        #     while curr != None:
        #         arr.append(curr.val)
        #         curr = curr.next
        
        # arr.sort()

        # if len(arr) == 0:                         # brute force
        #     return None

        # head = ListNode(arr[0])
        # curr = head

        # for i in range(1,len(arr)):
        #     curr.next = ListNode(arr[i])
        #     curr = curr.next

        # return head


        # if len(lists) == 0:
        #     return None

        # head = lists[0]                               # better approach
        # for i in range(1,len(lists)):
        #     head = self.merge(head,lists[i])
        # return head


        # if len(lists) == 0:
        #     return None

        pq = []                                          # optimal

        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(pq,(lists[i].val, i, lists[i]))

        res = ListNode(-1)
        curr = res

        while len(pq) != 0:
            val,i,node = heapq.heappop(pq)

            curr.next = node

            curr = curr.next

            if node.next != None:
                heapq.heappush(pq,(node.next.val, i, node.next))

        return res.next




