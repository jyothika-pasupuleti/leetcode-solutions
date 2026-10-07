class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in d:
                return [d[comp],i]
            d[nums[i]] = i