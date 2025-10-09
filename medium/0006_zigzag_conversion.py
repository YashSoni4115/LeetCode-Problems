"""
------------------------------------------------------------
LeetCode 6, Zigzag Conversion, difficulty medium, language python
Saved at 2025-10-08 20:58:06
------------------------------------------------------------
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1: 
            return s

        converted = ""
        pattern = 2*numRows - 2
        mapping = {}
        midpoint = int(pattern/2)

        for j in range(0, pattern):
            
            if midpoint >= j: 
                mapping[j] = j
            else: 
                mapping[j] = 2*midpoint - j
        
        rows = ['' for _ in range(midpoint + 1)]

        for i in range(0, len(s)):

            rows[mapping[i % pattern]] += s[i]
        
        return_str = ''

        for row in rows:
            return_str += row
        
        return return_str
