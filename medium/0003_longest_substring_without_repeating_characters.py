"""
------------------------------------------------------------
LeetCode 3, Longest Substring Without Repeating Characters, difficulty medium, language Python
Saved at 2025-10-08 20:53:15
------------------------------------------------------------
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left = 0
        right = 0
        largest = 0
        substr = ""

        while right < len(s) or (len(s) == 1 and right == 0):
            print(left, " ", right)
            if s[right] not in substr:
                substr += s[right]
                right += 1
                if right - left > largest:
                    largest = right - left
            else:
                if left == right:
                    right += 1
                    continue
                left += 1
                substr = s[left:right]
            print(substr)

        return largest
