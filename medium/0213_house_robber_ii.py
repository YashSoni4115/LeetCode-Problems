"""
------------------------------------------------------------
LeetCode 213, House Robber II, difficulty medium, language python
Saved at 2026-01-20 18:35:28
------------------------------------------------------------
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def linear_rob(houses):
            n = len(houses)
            if n == 0:
                return 0
            if n == 1:
                return houses[0]
            dp = [0] * n
            dp[0], dp[1] = houses[0], max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            
            return dp[-1]

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        return max(linear_rob(nums[1:]), linear_rob(nums[:-1]))
