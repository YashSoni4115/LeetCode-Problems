"""
------------------------------------------------------------
LeetCode 167, Two Sum II - Input Array Is Sorted, difficulty medium, language python
Saved at 2026-05-31 11:56:15
------------------------------------------------------------
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        total = numbers[l] + numbers[r]

        while total != target:
            if total < target:
                l += 1
            else:
                r -= 1
            total = numbers[l] + numbers[r]
        
        return [l+1,r+1] if total == target else -1
