class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #using mathematical formula
        # n = len(nums) 
        # s = sum(nums)
        # v = (n*(n+1))//2
        # return v-s     

        #using EX-OR 
        xor1 = len(nums)
        for i in range(1,len(nums)):
            xor1 = xor1 ^ i
        for j in range(len(nums)):
            xor1 = xor1 ^ nums[j]
        return xor1

