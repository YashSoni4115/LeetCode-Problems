"""
------------------------------------------------------------
LeetCode 1448, Count Good Nodes in Binary Tree, difficulty medium, language python
Saved at 2026-01-27 18:12:45
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0
        
        good = [0]

        def dfs(node, curr_max):
            
            if node.val >= curr_max:
                good[0] += 1
                curr_max = node.val
            
            if node.left:
                dfs(node.left, curr_max)

            if node.right:
                dfs(node.right, curr_max)
            
        dfs(root, root.val)

        return good[0]
