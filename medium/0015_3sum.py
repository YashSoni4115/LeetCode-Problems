"""
------------------------------------------------------------
LeetCode 15, 3Sum, difficulty medium, language python
Saved at 2025-10-08 21:02:15
------------------------------------------------------------
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triplets = []

        for i in range(0, len(nums) - 2):

            if nums[i] == nums[i-1] and i > 0:
                continue
            
            j, k = i + 1, len(nums) - 1

            while j < k:

                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    if [nums[i], nums[j], nums[k]] not in triplets:
                        triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                
                elif s < 0:
                    j += 1
                
                else:
                    k -= 1

        return triplets
