# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def start(self,curr1,curr2,d):
    #     while d != 0:
    #         curr2 = curr2.next
    #         d -= 1
    
    #     while curr1 != curr2:
    #         curr1 = curr1.next
    #         curr2 = curr2.next
    #     return curr1
   
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        # d = {}
        # curr1 = headA

        # while curr1 != None:                  # using dictionary
        #     d[curr1] = 1
        #     curr1 = curr1.next
        
        # curr2 = headB

        # while curr2 != None:
        #     if curr2 in d:
        #         return curr2
        #     curr2 = curr2.next

        # return None


        # curr1 = headA
        # len1 = 0

        # while curr1 != None:                            # using diff b/w the two linked lists
        #     len1 += 1
        #     curr1 = curr1.next
        
        # curr2 = headB
        # len2 = 0

        # while curr2 != None:
        #     len2 += 1
        #     curr2 = curr2.next
        
        # curr1 = headA
        # curr2 = headB

        # if len1 < len2:
        #     return self.start(curr1,curr2,len2 - len1)
        # else:
        #     return self.start(curr2,curr1,len1-len2)
        
        # curr1 = headA
        # curr2 = headB
        
        # while curr1 != curr2:

        #     if curr1 == None:
        #         curr1 = headB
        #     else:
        #         curr1 = curr1.next       # coming back to the l2 when l1 is none vice versa until both are equal
            
        #     if curr2 == None:
        #         curr2 = headA
        #     else:
        #         curr2 = curr2.next
            
        # return curr1


        curr1 = headA
        curr2 = headB

        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next

            if curr1 == curr2:
                return curr1

            if curr1 == None:
                curr1 = headB
            
            if curr2 == None:
                curr2 = headA

        return curr1


