class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        # nums.sort()
        # res = []

        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        # return res


        # nums.sort()
        # start = 0
        # end = -1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         start = i
        #         break
        # for i in range(len(nums)-1,-1,-1):
        #     if nums[i] == target:
        #         end = i
        #         break
        # res = []
        # for i in range(start,end+1):
        #     res.append(i)
        # return res

        
        
        # Finding the index for starting element
        # nums.sort()
        # low = 0
        # high = len(nums) - 1
        # start = 0

        # while low <= high:
        #     mid = (low+high) // 2
        #     if nums[mid] == target:
        #         start = mid
        #         high = mid-1
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1

        # finding index for ending element
        # low = 0
        # high = len(nums)-1
        # end = -1
        # while low <= high:
        #     mid = (low+high) // 2
        #     if nums[mid] == target:
        #         end = mid
        #         low = mid+1
        #     elif nums[mid] > target:
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        
        #res = []
        # for i in range(start,end+1):
        #     res.append(i)

        # return res


        no_of_min = 0
        target_freq = 0

        for i in range(len(nums)):
            if nums[i] == target:
                target_freq += 1
            elif nums[i] < target:
                no_of_min += 1
        res = []
        for i in range(no_of_min,no_of_min + target_freq):           # 3,1
            res.append(i)
        return res
