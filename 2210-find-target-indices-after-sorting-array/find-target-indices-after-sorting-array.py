class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res

        # low = 0
        # high = len(nums) - 1
        # res = []

        # while low <= high:
        #     mid = (low+high) // 2
        #     if nums[mid] == target:
        #         res.append(mid)
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # return res