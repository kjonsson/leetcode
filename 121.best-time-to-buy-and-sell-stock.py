#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0:
            return 0

        profit  = 0
        start_price = prices[0]
        curr_profit = 0

        for (idx, price) in enumerate(prices):
            curr_profit = price - start_price
            if curr_profit < 0:
                start_price = prices[idx]
                continue
                
            profit = max(curr_profit, profit)
            
        return profit
        
# @lc code=end

