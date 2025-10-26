"""
------------------------------------------------------------
LeetCode 19, Remove Nth Node From End of List, difficulty medium, language python
Saved at 2025-10-26 13:32:51
------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        values = []
        values.append(head.val)

        while head.next != None:
            head = head.next
            values.append(head.val)

        removed = []

        for i in range(len(values) - 1, -1, -1):
            if len(values) - n == i:
                continue
            removed.insert(0, values[i])

        if len(removed) == 0:
            return

        if len(removed) > 1:
            tail = ListNode(None, None)
        else:
            tail = None

        head.val, head.next = removed[0], tail

        if tail != None: 
            for i, val in enumerate(removed[1:]):
                tail.val = val
                if i != len(removed) - 2:
                    tail.next = ListNode(None, None)
                    tail = tail.next

        return head
