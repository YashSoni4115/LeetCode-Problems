"""
------------------------------------------------------------
LeetCode 125, Valid Palindrome, difficulty easy, language python
Saved at 2025-12-07 00:28:21
------------------------------------------------------------
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(x for x in s if x.isalpha() or x.isdigit()).lower()

        n = len(s)

        for i in range(n//2):
            if s[i] != s[n-i-1]:
                return False
        
        return True
