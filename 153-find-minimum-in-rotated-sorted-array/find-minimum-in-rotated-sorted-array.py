class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:                       #  [2,1]  [2,3,4,5,1]
            mid = (low+high) // 2
            
            if nums[mid] < nums[high]:
                high = mid

            else:
                low = mid + 1

        return nums[low]



            