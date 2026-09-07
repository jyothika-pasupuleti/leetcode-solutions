class Solution(object):
    def reverse(self,nums,i,j):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        n = len(nums)
        self.reverse(nums,n-k,n-1)
        self.reverse(nums,0,n-k-1)
        self.reverse(nums,0,n-1)


        # rotations = k%len(nums)
        # i = 0
        # while i < rotations:
        #     temp = nums[-1]
        #     for j in range(len(nums)-2,-1,-1):   # got TLE
        #         nums[j+1] = nums[j]
        #     nums[0] = temp

        #     i += 1


    


        