"""
------------------------------------------------------------
LeetCode 17, Letter Combinations of a Phone Number, difficulty medium, language python
Saved at 2025-10-08 21:05:21
------------------------------------------------------------
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        to_let = {
            "2":["a", "b", "c"], 
            "3":["d", "e", "f"], 
            "4":["g", "h", "i"], 
            "5":["j", "k", "l"], 
            "6":["m", "n", "o"], 
            "7":["p", "q", "r", "s"], 
            "8":["t", "u", "v"], 
            "9":["w", "x", "y", "z"]
            }
        
        if not digits:
            return []

        combinations =[""]

        for i, digit in enumerate(digits):
            
            new_combinations = []

            for letter in to_let[digit]:

                for combination in combinations:

                    new_combinations.append(combination + letter)

            combinations = new_combinations


        return combinations
