"""
------------------------------------------------------------
LeetCode 994, Rotting Oranges, difficulty medium, language python
Saved at 2026-03-28 14:17:33
------------------------------------------------------------
"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """def printGrid():
            s = ""
            for row in grid:
                for cell in row:
                    s += str(cell) + ' '
                s += '\n'
            print(s)"""
        
        m, n = len(grid), len(grid[0])

        minutes = 0

        change = [1]

        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        while len(change) != 0:
            change = []
            minutes += 1
            fresh = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        fresh += 1
                        for dr, dc in directions:
                            nr, nc = i + dr, j + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 2:
                                    change.append((i, j))
                                    break
            
            for i, j in change:
                grid[i][j] = 2
                fresh -= 1
            
            #printGrid()

        return minutes - 1 if fresh == 0 else -1
