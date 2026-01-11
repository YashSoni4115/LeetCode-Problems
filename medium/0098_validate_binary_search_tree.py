"""
------------------------------------------------------------
LeetCode 98, Validate Binary Search Tree, difficulty medium, language python
Saved at 2026-01-11 17:21:48
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def helper(node, high, low):
            if not node:
                return True
            
            if not low < node.val < high:
                return False
            
            return helper(node.left, node.val, low) and helper(node.right, high, node.val)
        
        return helper(root, float('inf'), float('-inf'))
