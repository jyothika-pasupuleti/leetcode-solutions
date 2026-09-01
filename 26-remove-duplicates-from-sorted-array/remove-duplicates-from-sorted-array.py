class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(1,len(nums)):
        #     if nums[count] != nums[i]:
        #         count += 1
        #         nums[count] = nums[i]
        # return count+1


        k = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        return k