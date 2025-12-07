"""
------------------------------------------------------------
LeetCode 56, Merge Intervals, difficulty medium, language python
Saved at 2025-12-07 00:33:26
------------------------------------------------------------
"""

from collections import deque

class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for current in intervals:
            last_merged = merged_intervals[-1]
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                merged_intervals.append(current)

        return merged_intervals
