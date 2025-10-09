"""
------------------------------------------------------------
LeetCode 9, Palindrome Number, difficulty easy, language Python
Saved at 2025-10-08 21:00:21
------------------------------------------------------------
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x)[::-1] == str(x)
