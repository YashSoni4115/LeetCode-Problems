"""
------------------------------------------------------------
LeetCode 16, 3Sum Closest, difficulty medium, language python
Saved at 2025-10-08 21:03:32
------------------------------------------------------------
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float("-inf")
        s = 0

        for i in range(0, len(nums) - 2):
            
            j, k = i + 1, len(nums) - 1

            while j < k:

                s = nums[i] + nums[j] + nums[k]

                if abs(s - target) <= abs(closest - target):
                    closest = s
                    if s == target: return s

                if s > target:
                    k -= 1
                else:
                    j += 1
        
        return closest
