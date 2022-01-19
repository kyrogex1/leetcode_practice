from typing import *

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximumProfit = 0
        lowestPriceSoFar = 10**4
        for price in prices:
            profit = price - lowestPriceSoFar
            if (profit > maximumProfit):
                maximumProfit = profit
            if (price < lowestPriceSoFar):
                lowestPriceSoFar = price

        return maximumProfit
  
array = [1,3]
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(array)
