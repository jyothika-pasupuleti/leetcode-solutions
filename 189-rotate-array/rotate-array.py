class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # k = k % len(nums)

        # while k > 0:
        #     val = nums.pop()
        #     nums.insert(0,val)
        #     k -= 1

        n = len(nums)
        r = k % n

        def reverse(left,right):
            while left < right :
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1
        reverse(0,n-1)
        reverse(0,r-1)
        reverse(r,n-1)
            
        
        