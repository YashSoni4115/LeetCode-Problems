"""
------------------------------------------------------------
LeetCode 55, Jump Game, difficulty medium, language python
Saved at 2026-01-06 15:46:53
------------------------------------------------------------
"""

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        furthest_i = 0
        end = len(nums) - 1

        for i in range(len(nums)):
            if i > furthest_i:
                return False

            furthest_i = max(furthest_i, i + nums[i])

            if furthest_i >= end:
                return True
        
        return True
