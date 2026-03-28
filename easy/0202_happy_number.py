"""
------------------------------------------------------------
LeetCode 202, Happy Number, difficulty easy, language python
Saved at 2026-03-28 14:19:06
------------------------------------------------------------
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited and n != 1:
            visited.add(n)
            n = str(n)
            total = 0
            for i in n:
                num = int(i)
                total += num * num
            n = total
        
        return True if n == 1 else False
