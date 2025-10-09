"""
------------------------------------------------------------
LeetCode 2221, Find Triangular Sum of an Array, difficulty medium, language python
Saved at 2025-10-08 21:11:23
------------------------------------------------------------
"""

class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        while len(nums) > 1:

            for i in range(len(nums) - 1):

                nums[i] = (nums[i] + nums[i + 1]) % 10
            
            nums.pop()
        
        return nums[0]
