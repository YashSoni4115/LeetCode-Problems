"""
------------------------------------------------------------
LeetCode 1514, Path with Maximum Probability, difficulty medium, language python
Saved at 2026-01-27 18:11:08
------------------------------------------------------------
"""

import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        
        graph = defaultdict(list)

        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        maxProb = [0.0] * n
        maxProb[start_node] = 1.0
        pq = [(-1.0, start_node)]

        while pq:
            currProb, node = heapq.heappop(pq)
            currProb = -currProb

            if node == end_node:
                return currProb
            
            for neighbour, prob in graph[node]:
                newProb = currProb * prob
                if newProb > maxProb[neighbour]:
                    maxProb[neighbour] = newProb
                    heapq.heappush(pq, (-newProb, neighbour))
        
        return maxProb[end_node] if maxProb[end_node] > 0 else 0.0
