"""
------------------------------------------------------------
LeetCode 3627, Maximum Median Sum of Subsequences of Size 3, difficulty medium, language python
Saved at 2026-03-28 14:19:46
------------------------------------------------------------
"""

class Solution(object):
    def maximumMedianSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cycles = len(nums) / 3
        nums.sort()
        total = 0
        for l in range(cycles):
            total += nums[-2*(l+1)]
        return total
