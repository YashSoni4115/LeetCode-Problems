"""
------------------------------------------------------------
LeetCode 23, Merge k Sorted Lists, difficulty hard, language python
Saved at 2025-10-26 13:38:17
------------------------------------------------------------
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """

        result_head = ListNode()
        result = result_head

        while lists:

            lists = [head for head in lists if head != None]

            if not lists:
                break

            lowest = float("inf")
            lowest_head = -1

            for i, head in enumerate(lists):

                if head.val < lowest:
                    lowest_head = i
                    lowest = head.val

            if lowest_head == -1:
                break

            result.next = lists[lowest_head]
            result = result.next

            lists[lowest_head] = lists[lowest_head].next
        
        return result_head.next
