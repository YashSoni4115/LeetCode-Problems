"""
------------------------------------------------------------
LeetCode 13, Roman to Integer, difficulty easy, language python
Saved at 2025-10-08 20:40:51
------------------------------------------------------------
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        value_mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prev_value = None
        for char in s:
            if prev_value:
                if value_mapping[prev_value] < value_mapping[char]:
                    value -= 2*value_mapping[prev_value]
            value += value_mapping[char]
            prev_value = char
        return value
