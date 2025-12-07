"""
------------------------------------------------------------
LeetCode 62, Unique Paths, difficulty medium, language python
Saved at 2025-12-07 00:36:36
------------------------------------------------------------
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if n == 1 or m == 1:
            return 1

        dp = [1] * n
        
        for r in range(1,m):
            for c in range(1,n): 
                dp[c] += dp[c - 1]
        
        return dp[-1]
