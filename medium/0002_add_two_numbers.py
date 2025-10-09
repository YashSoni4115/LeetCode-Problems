"""
------------------------------------------------------------
LeetCode 2, Add Two Numbers, difficulty medium, language Python
Saved at 2025-10-08 20:56:05
------------------------------------------------------------
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy1 = ListNode(next = l1)
        dummy2 = ListNode(next = l2)

        l1 = dummy1
        l2 = dummy2

        base = 1
        sum = 0

        while l1.next:
            l1 = l1.next
            sum += base * l1.val
            base *= 10
        
        base = 1

        while l2.next:
            l2 = l2.next
            sum += base * l2.val
            base *= 10

        while int(sum/base) != 0:
            base *= 10
        base /= 10

        sum_head = ListNode(val = int(sum/base))
        sum -= sum_head.val * base

        while base > 1:
            print(base)
            base /= 10
            sum_head = ListNode(val = int(sum/base), next = sum_head)
            sum -= sum_head.val * base
        
        return sum_head
