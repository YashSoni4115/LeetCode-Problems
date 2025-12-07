"""
------------------------------------------------------------
LeetCode 242, Valid Anagram, difficulty easy, language python
Saved at 2025-12-07 00:30:15
------------------------------------------------------------
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(s) == sorted(t)
