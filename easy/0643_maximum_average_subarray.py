"""
------------------------------------------------------------
LeetCode 643, Maximum Average Subarray, difficulty easy, language python
Saved at 2025-10-10 10:11:42
------------------------------------------------------------
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        if len(nums) == k:
            return float(sum(nums))/k

        l = 1

        total = float(sum(nums[:k]))

        max_avg = total/k

        while l + k <= len(nums):
            
            total += nums[l + k - 1] - nums[l - 1]

            avg = total/k

            max_avg = max(max_avg, avg)

            l += 1
        
        return max_avg
