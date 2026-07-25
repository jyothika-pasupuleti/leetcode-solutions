class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     current_sum = nums[i]
        #     for j in range(i+1,len(nums)):
        #         current_sum += nums[j]

        #     if current_sum > max_sum:
        #         max_sum = current_sum

        # return max_sum

        current_sum = 0
        max_sum = float('-inf')

        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


