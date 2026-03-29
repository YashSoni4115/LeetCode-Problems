"""
------------------------------------------------------------
LeetCode 25, Reverse Nodes in k-Group, difficulty hard, language python
Saved at 2026-03-29 12:28:04
------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            count = 0

            while curr and count < k:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
                count += 1

            return prev, node, curr

        n = 0
        node = head
        while node:
            n += 1
            node = node.next

        groups = n // k
        if groups == 0:
            return head

        dummy = ListNode(0, head)
        prevGroupTail = dummy
        curr = head

        for _ in range(groups):
            newHead, newTail, nextGroupStart = reverse(curr)

            prevGroupTail.next = newHead
            newTail.next = nextGroupStart

            prevGroupTail = newTail
            curr = nextGroupStart

        return dummy.next
