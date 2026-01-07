"""
------------------------------------------------------------
LeetCode 235, Lowest Common Ancestor of a Binary Search Tree, difficulty medium, language python
Saved at 2026-01-07 11:40:08
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > q.val:
            p, q = q, p

        def helper(node, l, r):
            if l.val <= node.val <= r.val:
                return node
            elif l.val > node.val:
                return helper(node.right, l, r)
            else:
                return helper(node.left, l, r)
        
        return helper(root, p, q)
