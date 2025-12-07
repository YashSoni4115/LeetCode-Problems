"""
------------------------------------------------------------
LeetCode 217, Conatins Duplicates, difficulty easy, language python
Saved at 2025-12-07 00:31:00
------------------------------------------------------------
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)
