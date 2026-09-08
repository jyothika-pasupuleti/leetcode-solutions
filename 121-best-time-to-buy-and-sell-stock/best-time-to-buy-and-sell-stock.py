class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = float('-inf')
        for price in prices:
            curr_profit  = 0
            if price < min_price:
                min_price = price
            curr_profit = price - min_price
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
