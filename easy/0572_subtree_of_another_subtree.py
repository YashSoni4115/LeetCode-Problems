"""
------------------------------------------------------------
LeetCode 572, Subtree of Another Subtree, difficulty easy, language python
Saved at 2026-01-20 18:33:24
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return dfs(root1.right, root2.right) and dfs(root1.left, root2.left)
        
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if dfs(subRoot, node):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return False
