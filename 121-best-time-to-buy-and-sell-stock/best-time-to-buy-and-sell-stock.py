class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         max_profit = max(max_profit,prices[j]-prices[i])
        #         # current_profit = prices[j]-prices[i] 
        #         # if max_profit > current_profit:
        #         #     max_profit = current_profit
        # if max_profit > 0:
        #     return max_profit
        # return 0


        min_price = prices[0]
        max = 0

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max:
                max = profit
        return max