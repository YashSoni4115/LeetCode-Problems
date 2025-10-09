"""
------------------------------------------------------------
LeetCode 18, 4Sum, difficulty medium, language Python
Saved at 2025-10-08 21:06:11
------------------------------------------------------------
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        hit_target = []

        nums.sort()

        for a in range(0, len(nums) - 3):

            for b in range(a + 1, len(nums) - 2):

                c, d = b + 1, len(nums) - 1

                while c < d:

                    s = nums[a] + nums[b] + nums[c] + nums[d]

                    if s == target:

                        if [nums[a], nums[b], nums[c], nums[d]] not in hit_target:
                            hit_target.append([nums[a], nums[b], nums[c], nums[d]])

                        c += 1
                        d -= 1
                    
                    elif s < target:

                        c += 1
                    
                    else:

                        d -= 1
        
        return hit_target
