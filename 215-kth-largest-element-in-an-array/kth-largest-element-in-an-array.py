class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # for i in range(k-1):  # 0,2
        #     num = max(nums)
        #     nums.remove(num)                     # got TLE
        # return max(nums)

        # nums.sort(reverse=True)                    # accepted
        # return nums[k-1]

        
        heap = [] 
        for num in nums:                        # [3,2,1,5,6,4]   [2,3] [2,3] [3,5] [5,6]  [5,6] (maintaining k largest elements)
            heapq.heappush(heap,num)                 # Optimal

            if len(heap) > k :
                heapq.heappop(heap)
                
        return heap[0]                              # [5,6]





