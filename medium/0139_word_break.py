"""
------------------------------------------------------------
LeetCode 139, Word Break, difficulty medium, language python
Saved at 2026-01-06 15:46:07
------------------------------------------------------------
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[i - len(word):i] == word and dp[i - len(word)] == True:
                    dp[i] = True
        
        return dp[-1]
