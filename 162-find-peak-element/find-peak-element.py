class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        # n = len(nums)

        # if n == 1 or nums[0] > nums[1]:
        #     return 0
    
        # for i in range(1,len(nums)-1):
        #     if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i 
        # return n - 1


        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left