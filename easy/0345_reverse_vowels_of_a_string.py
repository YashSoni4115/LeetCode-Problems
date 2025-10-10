"""
------------------------------------------------------------
LeetCode 345, Reverse Vowels of a String, difficulty easy, language python
Saved at 2025-10-10 10:14:00
------------------------------------------------------------
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        sv = []

        for char in s:
            if char.lower() in vowels:
                sv.append(char)
        
        sv = sv[::-1]

        i = 0

        result = ""

        for char in s:
            if char.lower() in vowels:
                result += sv[i]
                i += 1
            else:
                result += char
        
        return result
