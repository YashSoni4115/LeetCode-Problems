"""
------------------------------------------------------------
LeetCode 142, Reorder List, difficulty medium, language python
Saved at 2025-10-08 21:20:16
------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr, prev = slow, None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        f, s = head, prev

        while s.next != None:
            t1, t2 = f.next, s.next
            f.next = s
            s.next = t1
            f = t1
            s = t2
