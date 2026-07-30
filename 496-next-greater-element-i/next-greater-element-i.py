class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # l = []
        # for num in nums1:
        #     for i,v in enumerate(nums2):
        #         if v == num:
        #             while i+1 < len(nums2):
        #                 if nums2[i+1] > num:
        #                     l.append(nums2[i+1])
        #                     break
        #                 i += 1
        #             else:
        #                 l.append(-1)
        # return l



        #optimal code

        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]


