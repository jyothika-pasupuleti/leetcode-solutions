class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # low = 1
        # high = max(piles)

        # while low < high:
        #     mid = (low + high) // 2
        #     hours = 0

        #     for pile in piles:
        #         hours += math.ceil(pile / mid)

        #     if hours <= h:
        #         high = mid
        #     else:
        #         low = mid + 1

        # return low

        low = 1
        high = max(piles)

        while low < high:
            mid = (low+high) // 2
            time = self.calculatetime(piles,mid)

            if time <= h:
                high = mid
            else:
                low = mid + 1
        return low



    def calculatetime(self,piles,mid):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/mid)
        return hours

    