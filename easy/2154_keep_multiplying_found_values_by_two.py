"""
------------------------------------------------------------
LeetCode 2154, Keep Multiplying Found Values by Two, difficulty easy, language python
Saved at 2026-01-20 18:37:43
------------------------------------------------------------
"""

class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        nums = set(nums)
        
        while original in nums:
            original *= 2
        
        return original
