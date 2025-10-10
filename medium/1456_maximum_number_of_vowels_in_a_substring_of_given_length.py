"""
------------------------------------------------------------
LeetCode 1456, Maximum Number of Vowels in a Substring of Given Length, difficulty medium, language python
Saved at 2025-10-10 10:13:10
------------------------------------------------------------
"""

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        vowels = ["a", "e", "i", "o", "u"]

        count = 0

        for char in s[:k]:
            if char in vowels:
                count += 1

        if len(s) == k:
            return count
        
        max_count = count

        for i in range(1, len(s) - k + 1):

            if s[i - 1] in vowels:
                count -= 1
            
            if s[i + k - 1] in vowels:
                count += 1

            if count == k: 
                return k
            
            max_count = max(max_count, count)
        
        return max_count
