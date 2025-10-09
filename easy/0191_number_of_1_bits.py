"""
------------------------------------------------------------
LeetCode 191, Number of 1 Bits, difficulty easy, language python
Saved at 2025-10-08 21:21:49
------------------------------------------------------------
"""

import math

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 0:
            return 0

        digits = int(math.log(n, 2)) + 1
        
        base = 2**(digits - 1)

        count = 0

        while n > 0:
            if n - base >= 0:
                n -= base 
                count += 1
            base /= 2
        
        return count
