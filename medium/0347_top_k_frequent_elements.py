"""
------------------------------------------------------------
LeetCode 347, Top K Frequent Elements, difficulty medium, language python
Saved at 2026-01-20 18:36:49
------------------------------------------------------------
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}

        for num in nums:
            if num not in count.keys():
                count[num] = 1
            else:
                count[num] += 1
        
        most_frequent = heapq.nlargest(k, count.keys(), key=count.get)

        return most_frequent
