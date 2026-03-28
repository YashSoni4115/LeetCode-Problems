"""
------------------------------------------------------------
LeetCode 74, Search a 2D Matrix, difficulty medium, language python
Saved at 2026-03-28 14:18:41
------------------------------------------------------------
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])

        l1, r1 = 0, m - 1

        exists = False

        while l1 <= r1:
            m1 = (l1 + r1) // 2
            if matrix[m1][0] <= target <= matrix[m1][-1]:
                exists = True
                break
            elif matrix[m1][0] > target:
                r1 = m1 - 1
            else:
                l1 = m1 + 1
        if not exists:
            return False

        l2, r2 = 0, n - 1

        row = matrix[m1]

        while l2 <= r2:
            m2 = (l2 + r2) // 2
            
            if row[m2] == target:
                return True
            elif row[m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        
        return False
