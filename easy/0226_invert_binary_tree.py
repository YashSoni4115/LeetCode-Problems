"""
------------------------------------------------------------
LeetCode 226, Invert Binary Tree, difficulty easy, language python
Saved at 2026-01-13 17:34:29
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
