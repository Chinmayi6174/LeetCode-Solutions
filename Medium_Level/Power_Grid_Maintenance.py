class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # --- Inner DSU class ---
        class DSU:
            def __init__(self, n):
                self.parent = list(range(n + 1))
                self.rank = [0] * (n + 1)
            
            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]
            
            def union(self, a, b):
                pa, pb = self.find(a), self.find(b)
                if pa == pb:
                    return
                if self.rank[pa] < self.rank[pb]:
                    pa, pb = pb, pa
                self.parent[pb] = pa
                if self.rank[pa] == self.rank[pb]:
                    self.rank[pa] += 1
        
        # --- Step 1: Build connected components ---
        dsu = DSU(c)
        for u, v in connections:
            dsu.union(u, v)
        
        comp_members = defaultdict(list)
        for i in range(1, c + 1):
            comp_members[dsu.find(i)].append(i)
        
        # --- Step 2: Track online stations per component ---
        online_sets = {root: SortedList(members) for root, members in comp_members.items()}
        online = [True] * (c + 1)
        
        res = []
        
        # --- Step 3: Process queries ---
        for t, x in queries:
            if t == 1:
                if online[x]:
                    res.append(x)
                else:
                    root = dsu.find(x)
                    s = online_sets[root]
                    res.append(s[0] if s else -1)
            else:  # [2, x]
                if online[x]:
                    online[x] = False
                    root = dsu.find(x)
                    online_sets[root].remove(x)
        
        return res
