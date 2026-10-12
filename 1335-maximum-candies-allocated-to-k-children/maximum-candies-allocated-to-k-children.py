class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:

        low = 1
        high = max(candies)
        ans = 0

        while low <= high:
            mid = (low + high ) // 2

            count = 0
            for candy in candies:
                count += candy // mid
            
            if count >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
