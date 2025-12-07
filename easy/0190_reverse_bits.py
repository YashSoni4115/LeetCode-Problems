"""
------------------------------------------------------------
LeetCode 190, Reverse Bits, difficulty easy, language python
Saved at 2025-12-07 00:35:32
------------------------------------------------------------
"""

class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = bin(n)[2:]
        s = s[::-1]
        while len(s) != 32:
            s += "0"
        return int(s,2)
