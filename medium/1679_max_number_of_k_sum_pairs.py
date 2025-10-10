"""
------------------------------------------------------------
LeetCode 1679, Max Number of K-Sum Pairs, difficulty medium, language python
Saved at 2025-10-10 10:09:58
------------------------------------------------------------
"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        nums.sort()

        l, r = 0, len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]

            if s < k:
                l += 1

            elif s > k:
                r -= 1
            
            else:
                count += 1
                l += 1
                r -= 1
        
        return count
