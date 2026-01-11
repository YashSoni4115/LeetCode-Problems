"""
------------------------------------------------------------
LeetCode 57, Insert Interval, difficulty medium, language python
Saved at 2026-01-11 17:22:48
------------------------------------------------------------
"""

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        def ifOverlappingMerge(interval1, interval2):
            if interval2[0] <= interval1[0] and interval1[1] <= interval2[1]:
                return interval2
            if interval2[0] >= interval1[0] and interval1[1] >= interval2[1]:
                return interval1
            if interval2[0] <= interval1[0] <= interval2[1]:
                return [interval2[0], interval1[1]]
            if interval2[0] <= interval1[1] <= interval2[1]:
                return [interval1[0], interval2[1]]
            else:
                return False

        result = []
        new_merged = False

        for interval in intervals:
            merged = ifOverlappingMerge(interval, newInterval)
            if merged:
                newInterval = merged
            else:
                if newInterval[0] < interval[0] and not new_merged:
                    new_merged = True
                    result.append(newInterval)
                result.append(interval)
        
        if not new_merged:
            result.append(newInterval)

        return result
