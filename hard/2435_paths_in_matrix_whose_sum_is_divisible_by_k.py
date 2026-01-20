"""
------------------------------------------------------------
LeetCode 2435, Paths in Matrix Whose Sum Is Divisible by K, difficulty hard, language python
Saved at 2026-01-20 18:39:12
------------------------------------------------------------
"""

class Solution(object):
    def numberOfPaths(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        mem = {}

        def dfs(r, c, sum):
            if r == m - 1 and c == n - 1:
                return 1 if (sum + grid[r][c]) % k == 0 else 0

            key = (r, c, sum % k)

            if key in mem:
                return mem[key]

            count = 0

            if r < m - 1:
                count += dfs(r + 1, c, sum + grid[r][c])

            if c < n - 1:
                count += dfs(r, c + 1, sum + grid[r][c])

            count %= MOD
            mem[key] = count
            return count

        MOD = 10**9 + 7
        return dfs(0, 0, 0)
