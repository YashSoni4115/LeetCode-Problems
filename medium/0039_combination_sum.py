"""
------------------------------------------------------------
LeetCode 39, Combination Sum, difficulty medium, language python
Saved at 2025-10-08 21:18:06
------------------------------------------------------------
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        result = []

        def recursiveSum(remaining, stack, start):

            if remaining == 0:
                result.append(list(stack))
                return

            elif remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                stack.append(candidates[i])

                recursiveSum(remaining - candidates[i], stack, i)

                stack.pop()
            
        recursiveSum(target, [], 0)
        return result
