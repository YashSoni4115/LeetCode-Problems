"""
------------------------------------------------------------
LeetCode 128, Longest Consecutive Sequence, difficulty medium, language python
Saved at 2025-10-08 21:13:56
------------------------------------------------------------
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        num_set = set(nums)
        longest = 0
        current = 0

        for num in num_set:

            if num - 1 not in num_set:
                current = 1
                
                while num + 1 in num_set:
                    num += 1
                    current += 1
            
                longest = max(longest, current)
        
        return longest
