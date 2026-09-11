class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i]*nums[i]
        # nums.sort()                         # T.C : O(n log n)
        # return nums
        res = [0]*len(nums)
        pointer = len(nums)-1
        left = 0
        right = len(nums)-1
        for i in range(len(nums)):
            if abs(nums[right]) > abs(nums[left]):
                res[pointer] = nums[right] ** 2   
                right -= 1
                pointer -= 1
            else:
                res[pointer] = nums[left] ** 2
                left += 1
                pointer -= 1
        return res





        