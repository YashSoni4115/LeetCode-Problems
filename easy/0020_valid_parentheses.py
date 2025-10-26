"""
------------------------------------------------------------
LeetCode 20, Valid Parentheses, difficulty easy, language python
Saved at 2025-10-26 13:33:52
------------------------------------------------------------
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        mapping = {'(':')', '{':'}', '[':']'}

        stack = []

        for char in s:
            if char in mapping.keys():
                stack.append(char)
            else:
                try:
                    if char == mapping[stack.pop()]:
                        continue
                    return False
                except Exception:
                    return False

        return len(stack) == 0
