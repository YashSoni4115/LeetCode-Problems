"""
------------------------------------------------------------
LeetCode 297, Serialize and Deserialize Binary Tree, difficulty hard, language python
Saved at 2025-10-26 13:41:51
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ""

        result = []

        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("N")

        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return
        
        vals = data.split(" ")
        vals.pop()
        vals = deque(vals)
        root = TreeNode(int(vals.popleft()))
        queue = deque([root])

        while vals:
            node = queue.popleft()

            left_val = vals.popleft()
            if left_val != "N":
                node.left = TreeNode(int(left_val))
                queue.append(node.left)
            else:
                node.left = None

            if vals:
                right_val = vals.popleft()
                if right_val != "N":
                    node.right = TreeNode(int(right_val))
                    queue.append(node.right)
                else:
                    node.right = None

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
