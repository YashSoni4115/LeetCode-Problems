"""
------------------------------------------------------------
LeetCode 338, Counting Bits, difficulty easy, language python
Saved at 2026-01-20 18:33:59
------------------------------------------------------------
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n + 1):
            ibin = bin(i)[2:]
            bits = 0
            for char in ibin:
                if char == '1':
                    bits += 1
            result.append(bits)
        
        return result
