class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i],0) + 1
        for key,value in d.items():
            if value >= n/2:
                return key
