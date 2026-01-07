"""
------------------------------------------------------------
LeetCode 91, Decode Ways, difficulty medium, language py
Saved at 2026-01-07 11:38:04
------------------------------------------------------------
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        codes = set()
        for code in range(26):
            codes.add(str(code + 1))
        
        for i in range(1, len(s)):
            if s[i] in codes and s[i-1:i+1] in codes:
                dp[i + 1] = dp[i] + dp[i - 1]
            elif s[i] in codes:
                dp[i + 1] = dp[i]
            elif s[i-1:i+1] in codes:
                dp[i + 1] = dp[i - 1]
        return dp[-1]
