"""
------------------------------------------------------------
LeetCode 208, Implement Trie (Prefix Tree), difficulty medium, language python
Saved at 2026-01-20 18:38:18
------------------------------------------------------------
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.wordEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.wordEnd

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
