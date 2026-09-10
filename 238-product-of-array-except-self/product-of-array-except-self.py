class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # answer = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             product *= nums[j]    # T.C. : O(n)^2     got TLE
        #     answer.append(product)
        # return answer

        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        prefix_product = 1
        for i in range(len(nums)):
            prefix[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suffix_product
            suffix_product *= nums[i]
            
        # print(prefix)
        # print(suffix)
        
        answer = []
        for i in range(len(suffix)):
            answer.append(prefix[i] * suffix[i])

        return answer





