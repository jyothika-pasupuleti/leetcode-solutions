class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num

        result = 0
        for num in nums:
            result ^= num
        return result

        #if nums = [2,2,1,3,1,4]  --> return unique values in the list format
        # d = {}
        # for val in nums:
        #     d[val] = d.get(value,0)+1
        # for key,value in d:
        #     if value == 1:
        #         l.append(key)


        