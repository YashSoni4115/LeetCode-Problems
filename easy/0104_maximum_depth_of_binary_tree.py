"""
------------------------------------------------------------
LeetCode 104, Maximum Depth of Binary Tree, difficulty easy, language python
Saved at 2026-01-07 11:55:13
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return 1 + max(l, r)
        
        return dfs(root)
