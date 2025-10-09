"""
------------------------------------------------------------
LeetCode 7, Reverse Integer, difficulty medium, language Python
Saved at 2025-10-08 20:59:23
------------------------------------------------------------
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        negative = False

        if x < 0:
            negative = True
            x = -x

        base = 1

        digits = []

        while int(x/base) >= 10:
            base *= 10

        int_size = base

        while base >= 1:
            digits.append(int(x/base))
            x -= int(x/base) * base
            base /= 10

        digits = digits[::-1]

        reversed = 0

        for digit in digits:
            if (2**31 - reversed) < (digit * int_size): return 0
            reversed += digit * int_size
            int_size /= 10
        
        if negative: reversed = -reversed

        return reversed
