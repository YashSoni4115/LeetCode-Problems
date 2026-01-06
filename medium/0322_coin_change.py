"""
------------------------------------------------------------
LeetCode 322, Coin Change, difficulty medium, language python
Saved at 2026-01-06 15:45:21
------------------------------------------------------------
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        totals = [amount + 1] * (amount + 1)
        totals[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    totals[i] = min(totals[i], totals[i - coin] + 1)
        
        if totals[-1] == amount + 1:
            return -1
        
        return totals[-1]
