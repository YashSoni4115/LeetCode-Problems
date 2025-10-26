"""
------------------------------------------------------------
LeetCode 139, Word Break, difficulty medium, language python
Saved at 2025-10-26 13:28:58
------------------------------------------------------------
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        wordDict = set(wordDict)

        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s) + 1):

            for j in range(0, i):
                
                print(str(s[:j-1]), str(s[j:i]), dp[j])

                if dp[j] and s[j:i] in wordDict:

                    dp[i] = True

                    break
        
        return dp[len(s)]
