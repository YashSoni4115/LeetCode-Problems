"""
------------------------------------------------------------
LeetCode 5, Longest Palindromic String, difficulty medium, language python
Saved at 2025-10-08 21:15:50
------------------------------------------------------------
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        b, e = 0, 0

        def expandCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return right - left - 1

        for i in range(0, len(s) - 1):
            ith_palindrome = max(expandCenter(i, i), expandCenter(i, i + 1))

            if ith_palindrome > e - b:
                e = i + ith_palindrome // 2
                b = i - (ith_palindrome - 1) // 2
        
        return s[b:e + 1]
