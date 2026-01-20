"""
------------------------------------------------------------
LeetCode 238, Product of Array Except Self, difficulty medium, language python
Saved at 2026-01-20 18:32:38
------------------------------------------------------------
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefixes, suffixes = [1] * n, [1] * n
        
        for i in range(1, n):
            prefixes[i] = prefixes[i-1] * nums[i-1]
            suffixes[n-i-1] = suffixes[n-i] * nums[n-i]
        
        result = []

        for i in range(n):
            result.append(prefixes[i]*suffixes[i])
        
        return result
