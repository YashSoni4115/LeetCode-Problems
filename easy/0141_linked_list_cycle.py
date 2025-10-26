"""
------------------------------------------------------------
LeetCode 141, Linked List Cycle, difficulty easy, language python
Saved at 2025-10-26 13:30:02
------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return False

        visited = set()

        while head.next != None:
            if head.next not in visited:
                head = head.next
                visited.add(head)
            else:
                return True
        
        return False
