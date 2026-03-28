"""
------------------------------------------------------------
LeetCode 40, Combination Sum, difficulty medium, language python
Saved at 2026-03-28 14:18:05
------------------------------------------------------------
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []

        candidates.sort()

        def backtrack(start, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if num > remaining:
                    break
                backtrack(i + 1, path + [num], remaining - num)
        
        backtrack(0, [], target)

        return result
