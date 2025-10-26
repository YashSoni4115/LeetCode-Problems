"""
------------------------------------------------------------
LeetCode 295, Find Median from Data Stream, difficulty hard, language python
Saved at 2025-10-26 13:40:00
------------------------------------------------------------
"""

import heapq

class MedianFinder(object):

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.max_heap, -num)

        if self.max_heap and self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.min_heap) < len(self.max_heap):
            return float(-self.max_heap[0])
        else:
            return (float(self.min_heap[0]) - float(self.max_heap[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
