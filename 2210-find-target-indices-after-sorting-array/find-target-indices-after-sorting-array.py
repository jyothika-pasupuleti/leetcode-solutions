class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        # return res

        low = 0
        high = len(nums) - 1
        start = 0

        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                start = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = len(nums)-1
        end = -1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] == target:
                end = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        
        
        for i in range(start,end+1):
            res.append(i)

        return res