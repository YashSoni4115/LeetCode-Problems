"""
------------------------------------------------------------
LeetCode 33, Search in Rotated Sorted Array, difficulty medium, language python
Saved at 2025-10-26 13:37:30
------------------------------------------------------------
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        low, high = 0, len(nums) - 1

        while low <= high:

            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            
            if nums[high] >= nums[mid]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            else:
                if nums[mid] > target and target >= nums[low]:
                    high = mid - 1
                else:
                    low = mid + 1
        
        return -1
