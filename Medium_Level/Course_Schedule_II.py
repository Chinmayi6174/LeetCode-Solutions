from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        pathVisited = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        # Build graph
        for course, pre in prerequisites:
            graph[pre].append(course)
        res = []
        def dfs(node):
            visited[node] = 1
            pathVisited[node] = 1
            for nei in graph[node]:
                if visited[nei] == 0:
                    if dfs(nei):
                        return True
                elif pathVisited[nei] == 1:
                    return True   # cycle detected
            pathVisited[node] = 0
            res.append(node)
            return False
        # Run DFS on all nodes
        for i in range(numCourses):
            if visited[i] == 0:
                if dfs(i):
                    return []
        return res[::-1]
