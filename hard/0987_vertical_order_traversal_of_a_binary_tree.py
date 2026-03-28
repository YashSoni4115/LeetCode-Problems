"""
------------------------------------------------------------
LeetCode 987, Vertical Order Traversal of a Binary Tree, difficulty hard, language python
Saved at 2026-03-28 14:14:44
------------------------------------------------------------
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = {}
        
        def dfs(node, coord = (0,0)):
            if not node:
                return
            
            depth, width = coord
            
            if width in order.keys():
                order[width].append((depth, node.val))
            else:
                order[width] = [(depth, node.val)]
            
            dfs(node.right, (depth + 1, width + 1))
            dfs(node.left, (depth + 1, width - 1))

        dfs(root)

        result = []

        keys = list(order.keys())
        keys.sort()
        
        for width in keys:
            curr_width = []
            node_list = order[width]
            node_list.sort(key=lambda x: (x[0], x[1]))
            
            for node in node_list:
                curr_width.append(node[1])
            result.append(curr_width)
        
        return result
