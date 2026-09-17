class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for i in range(len(nums)):
        #     d[i] = 1

        if not nums:
            return 0
        nums.sort()
        max_count = 1
        curr_count = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:    # [1,2,6,7,8]
                curr_count += 1
            elif nums[i] - nums[i-1] != 0:
                curr_count = 1
            if curr_count > max_count:
                max_count = curr_count
        return max_count                     # [0,1,1,2]




        