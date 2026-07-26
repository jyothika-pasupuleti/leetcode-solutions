class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # rotations = k % n
        # for _ in range(rotations):
        #     last_ele = nums.pop()
        #     nums.insert(0,last_ele)           raised TLE



        k = k % len(nums)
    
        nums[:] = nums[-k:] + nums[:-k]



        