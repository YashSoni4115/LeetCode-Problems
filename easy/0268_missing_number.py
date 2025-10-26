"""
------------------------------------------------------------
LeetCode 268, Missing Number, difficulty easy, language python
Saved at 2025-10-26 13:31:21
------------------------------------------------------------
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = set(nums)

        for num in range(0, len(nums)):

            if num not in nums:
                return num
        
        return len(nums)
