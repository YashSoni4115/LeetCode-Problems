"""
------------------------------------------------------------
LeetCode 198, House Robber, difficulty medium, language python
Saved at 2025-12-07 00:34:52
------------------------------------------------------------
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = [None for _ in range(len(nums) + 1)]
        dp[0], dp[1] = 0, nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i - 1]) 
        
        return dp[len(nums)]
