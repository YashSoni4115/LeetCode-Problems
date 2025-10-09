"""
------------------------------------------------------------
LeetCode 647, Palindromic Substrings, difficulty medium, language python
Saved at 2025-10-08 21:17:08
------------------------------------------------------------
"""

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        def aroundCenter(b, e):
            count = 0
            while b >= 0 and e < len(s) and s[b] == s[e]:
                b -= 1
                e += 1
                count += 1
            return count 
        
        count = 0

        for i in range(0, len(s)):
            count += aroundCenter(i, i)
            count += aroundCenter(i, i + 1)
        
        return count
