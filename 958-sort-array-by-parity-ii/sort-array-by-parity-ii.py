class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        even = 0
        odd = 1
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                res[even] = nums[i]
                even += 2
            else:
                res[odd] = nums[i]
                odd += 2
        return res

        