"""
------------------------------------------------------------
LeetCode 207, Course Schedule, difficulty medium, language python
Saved at 2026-01-20 18:34:46
------------------------------------------------------------
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        visited = [0] * numCourses

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            visited[node] = 2
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
