"""
------------------------------------------------------------
LeetCode 73, Set Matrix Zeroes, difficulty medium, language python
Saved at 2025-12-07 00:31:55
------------------------------------------------------------
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        zeros = []
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i,j))
        
        for row, col in zeros:
            for i in range(m):
                matrix[i][col] = 0
            for j in range(n):
                matrix[row][j] = 0
