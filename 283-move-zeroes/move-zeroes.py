class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for num in nums:
        #     if num == 0:
        #         nums.remove(0)
        #         nums.append(0)
        

        non_zeroes = [num for num in nums if num != 0]
        n = len(nums)
        zeroes = n-len(non_zeroes)

        result = non_zeroes + [0] * zeroes

        for i in range(len(nums)):
            nums[i] = result[i]

