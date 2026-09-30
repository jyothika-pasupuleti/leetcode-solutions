class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = -1
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        end = -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                end = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return [start,end]


