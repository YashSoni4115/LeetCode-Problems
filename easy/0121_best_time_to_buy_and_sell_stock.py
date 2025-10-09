"""
------------------------------------------------------------
LeetCode 121, Best Time to Buy and Sell Stock, difficulty easy, language python
Saved at 2025-10-08 21:20:58
------------------------------------------------------------
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_p = 0
        min_price = prices[0]
        
        for price in prices:
            min_price = min(price, min_price)
            p = price - min_price
            max_p = max(max_p, p)
        
        return max_p
