"""
------------------------------------------------------------
LeetCode 3100, Water Bottles II, difficulty medium, language python
Saved at 2025-10-08 21:12:17
------------------------------------------------------------
"""

class Solution(object):
    def maxBottlesDrunk(self, n, ex):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """

        d = n
        e = n

        while e >= ex:

            e -= ex - 1

            ex += 1
            
            d += 1

        return d
