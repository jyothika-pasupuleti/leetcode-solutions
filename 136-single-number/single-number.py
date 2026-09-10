class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d = {}
        # for num in nums:
        #     d[num] = d.get(num,0) + 1
        # for k,v in d.items():
        #     if v == 1:
        #         return k

        val = nums[0]
        for num in nums[1:]:
            val = val ^ num
        return val



        