class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for num in nums1:
            for i,v in enumerate(nums2):
                if v == num:
                    while i+1 < len(nums2):
                        if nums2[i+1] > num:
                            l.append(nums2[i+1])
                            break
                        i += 1
                    else:
                        l.append(-1)
        return l

