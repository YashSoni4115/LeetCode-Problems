"""
------------------------------------------------------------
LeetCode 1768, Merge Strings Alternately, difficulty easy, language python
Saved at 2025-10-10 10:06:10
------------------------------------------------------------
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        result = ""

        if len(word1) < len(word2):
            end = word2[len(word1):]
            word2 = word2[:len(word1)]
        
        elif len(word2) < len(word1):
            end = word1[len(word2):]
            word1 = word1[:len(word2)]
        
        while word1 != "":
            result += word1[0] + word2[0]
            word1, word2 = word1[1:], word2[1:]
        
        if 'end' in locals():
            return result + end
        
        return result
