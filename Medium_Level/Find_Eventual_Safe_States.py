class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        revg=[[] for i in range(n)]
        out=[0]*n
        for u in range(n):
            out[u] = len(graph[u])
            for v in graph[u]:
                revg[v].append(u)
        q=[]
        for i in range(n):
            if out[i]==0:
                q.append(i)
        safe=[False]*n
        while q:
            node = q.pop(0)
            safe[node]=True
            for nei in revg[node]:
                out[nei]-=1
                if out[nei]==0:
                    q.append(nei)
        res=[]
        for i in range(n):
            if safe[i]:
                res.append(i)
        return res


#another approach
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        vis = [0] * n
        pathVis = [0] * n
        safe = [0] * n
        def dfs(node):
            vis[node] = 1
            pathVis[node] = 1
            for nei in graph[node]:
                if vis[nei] == 0:
                    if dfs(nei):
                        return True
                elif pathVis[nei]:
                    return True
            pathVis[node] = 0
            safe[node] = 1
            return False
        for i in range(n):
            if vis[i] == 0:
                dfs(i)
        return [i for i in range(n) if safe[i]]
