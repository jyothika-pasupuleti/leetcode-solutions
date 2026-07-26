class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # l = [num for num in set(nums1) if num in set(nums2)]

        # return l


        return list(set(nums1) & set(nums2))
        