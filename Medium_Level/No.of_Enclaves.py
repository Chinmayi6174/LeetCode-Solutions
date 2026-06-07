from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            vis[i][j] = 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = i + dr
                nc = j + dc
                if (0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1 and vis[nr][nc] == 0):
                    dfs(nr, nc)
        n = len(grid)
        m = len(grid[0])
        vis = [[0] * m for _ in range(n)]
        # Traverse boundary cells
        for i in range(n):
            for j in range(m):
                if ((i == 0 or i == n - 1 or j == 0 or j == m - 1) and grid[i][j] == 1 and vis[i][j] == 0):
                    dfs(i, j)
        # Count unvisited land cells
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and vis[i][j] == 0:
                    count += 1
        return count
