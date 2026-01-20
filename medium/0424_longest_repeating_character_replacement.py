"""
------------------------------------------------------------
LeetCode 424, Longest Repeating Character Replacement, difficulty medium, language python
Saved at 2026-01-20 18:36:02
------------------------------------------------------------
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        char_count = defaultdict(int)
        
        left = 0
        max_count = 0
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] += 1
            max_count = max(max_count, char_count[s[right]])

            while (right - left + 1) - max_count > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
