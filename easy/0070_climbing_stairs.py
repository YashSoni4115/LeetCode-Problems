"""
------------------------------------------------------------
LeetCode 70, Climbing Stairs, difficulty easy, language python
Saved at 2025-12-07 00:37:40
------------------------------------------------------------
"""

class Solution(object):

    timeMap = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        1   1  2  3  5. 8
        [0, 1, 2, 3, 4, 5]
        """
        if n ==0 or n == 1:
            return 1

        if n == 2:
            return 2

        dp = [1] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        
        for i in range(2, n+1):
            print(i)
            dp[i] = dp[i-1] + dp[i - 2]
        
        return dp[n]
