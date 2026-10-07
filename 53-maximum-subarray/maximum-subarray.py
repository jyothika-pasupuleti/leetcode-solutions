class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        curr = 0

        for i in range(len(nums)):
            curr = max(curr+nums[i],nums[i])
            max_sum = max(curr,max_sum)

        return max_sum