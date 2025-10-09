"""
------------------------------------------------------------
LeetCode 133, Clone Graph, difficulty medium, language python
Saved at 2025-10-08 21:14:57
------------------------------------------------------------
"""

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if node == None:
            return None

        clones = {}

        def dfs(n):

            if n in clones:
                return clones[n]
            
            clone = Node(val = n.val)
            clones[n] = clone

            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
