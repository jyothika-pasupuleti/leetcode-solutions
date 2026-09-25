class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # for i in range(k-1):  # 0,2
        #     num = max(nums)
        #     nums.remove(num)                     # got TLE
        # return max(nums)

        nums.sort(reverse=True)
        return nums[k-1]
