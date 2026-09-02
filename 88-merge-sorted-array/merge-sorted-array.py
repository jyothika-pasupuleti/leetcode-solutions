class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # index = 0
        # for i in range(m,len(nums1)):      # TC : O((m+n) log (m+n))  SC : O(1)
        #     nums1[i] = nums2[index]
        #     index += 1
        # nums1.sort()

        # for i in range(n):
        #     nums1[m+i] = nums2[i]          # TC : O((m+n) log (m+n))  SC : O(1)
        # nums1.sort()

        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])        # T.C: O(m+n)  S.C : O(m+n)
                j += 1
        while i < m:
            res.append(nums1[i])
            i += 1
        while j < n:
            res.append(nums2[j])
            j += 1
        for i in range(m+n):
            nums1[i] = res[i]
            