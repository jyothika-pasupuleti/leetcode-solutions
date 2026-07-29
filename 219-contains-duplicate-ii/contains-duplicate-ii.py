class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False                                  # GOT TLE
                
        d = {}
        for i,num in enumerate(nums):
            if num in d:
                if abs(d[num]-i) <= k:
                    return True
            d[num] = i

        return False

