class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        smallest = nums[0]
        largest = nums[0]
        for num in nums[1:]:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num
        d = 1
        for i in range(2,smallest+1):
            if smallest % i == 0 and largest %  i == 0:
                d = i
        return d

