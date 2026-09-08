class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # min_price = prices[0]
        # max_profit = 0
        # for price in prices:
        #     curr_profit  = 0
        #     if price < min_price:            # considering min cost price
        #         min_price = price
        #     curr_profit = price - min_price
        #     if curr_profit > max_profit:
        #         max_profit = curr_profit
        # return max_profit




        max_selling_price = prices[-1]
        max_profit = 0
        for i in range(len(prices)-2,-1,-1):
            
            curr_profit = max_selling_price - prices[i]        # considering max selling price
            if curr_profit > max_profit:
                max_profit = curr_profit
            if prices[i] > max_selling_price:
                max_selling_price = prices[i]
        return max_profit

