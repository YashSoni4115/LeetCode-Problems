"""
------------------------------------------------------------
LeetCode 66, Plus One, difficulty easy, language python
Saved at 2026-05-31 11:57:27
------------------------------------------------------------
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            carry = 0
            digits[i] += 1
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                break
        
        if carry == 1:
            digits.insert(0,1)
        
        return digits
