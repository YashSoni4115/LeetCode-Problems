"""
------------------------------------------------------------
LeetCode 48, Rotate Image, difficulty medium, language python
Saved at 2025-10-26 13:39:08
------------------------------------------------------------
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        for row in range(0, n - 1):
            for col in range(1, n):
                if row == col or row > col:
                    continue
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp

        for row in matrix:
            for col in range(0, n//2):
                temp = row[col]
                row[col] = row[n - col - 1]
                row[n - col - 1] = temp

"""
(2,1)
(0,0), (1,1), (2,2), (3,3)
"""
