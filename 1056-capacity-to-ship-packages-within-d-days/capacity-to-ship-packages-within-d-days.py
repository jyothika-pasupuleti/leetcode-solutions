class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        least_wt_capacity = max(weights)

        while low <= high:
            mid = (low+high) // 2
            temp = mid
            c_days = 1
        
            for weight in weights:            # [1,2,3,1,1], days = 4  9
                if weight > temp:
                    c_days += 1
                    temp = mid
                temp -= weight
                

            if c_days <= days:
                least_wt_capacity = mid
                high = mid - 1
            else:
                low = mid + 1

        return least_wt_capacity



