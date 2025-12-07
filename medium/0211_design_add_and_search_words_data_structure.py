"""
------------------------------------------------------------
LeetCode 211, Design Add and Search Words Data Structure, difficulty medium, language python
Saved at 2025-12-07 00:34:16
------------------------------------------------------------
"""

class WordDictionary(object):

    def __init__(self):
        self.words = set()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.words.add(word)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if "." not in word:
            return word in self.words
        
        length = len(word)

        for item in self.words:
            if length != len(item):
                continue

            word_exists = True

            for i in range(len(item)):
                if not word_exists:
                    break
                if word[i] == ".":
                    continue
                elif word[i] != item[i]:
                    word_exists = False
                
            if word_exists:
                return True
        
        return False
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
