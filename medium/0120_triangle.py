"""
------------------------------------------------------------
LeetCode 120, Triangle, difficulty medium, language Python
Saved at 2025-10-08 21:07:23
------------------------------------------------------------
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(0, len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])

        return triangle[0][0]
