"""
------------------------------------------------------------
LeetCode 200, Number of Islands, difficulty medium, language python
Saved at 2025-12-07 00:32:39
------------------------------------------------------------
"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        count = 0
        
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            grid[i][j] = "0"
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == "1":
                        dfs(nr, nc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        
        return count
