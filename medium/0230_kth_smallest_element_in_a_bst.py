"""
------------------------------------------------------------
LeetCode 230, Kth Smallest Element in a BST, difficulty medium, language python
Saved at 2025-10-26 13:40:57
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        if not root:
            return 
        
        node = root
        vals = []

        def inOrder(root):
            if not root or len(vals) == k:
                return
            inOrder(root.left)
            vals.append(root.val)
            inOrder(root.right)
        
        inOrder(root)

        return vals[k - 1]
