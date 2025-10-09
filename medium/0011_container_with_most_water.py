"""
------------------------------------------------------------
LeetCode 11, Container With Most Water, difficulty medium, language python
Saved at 2025-10-08 21:01:24
------------------------------------------------------------
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0

        left, right = 0, len(height) - 1

        while left < right:
            width = right - left

            current_height = min(height[left], height[right])
            current_area = width*current_height

            max_water = max(max_water, current_area)

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return max_water
