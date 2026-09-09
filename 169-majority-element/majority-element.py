class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n = len(nums)
        # d = {}
        # for i in range(len(nums)):
        #     d[nums[i]] = d.get(nums[i],0) + 1
        # for key,value in d.items():
        #     if value >= n/2:
        #         return key


        candidate = 0
        vote = 0
        for num in nums:
            if vote == 0:
                candidate = num
            if num == candidate:
                vote += 1
            else:
                vote -= 1
        return candidate


        
