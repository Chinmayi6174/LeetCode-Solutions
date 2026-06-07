from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n= len(grid)
        m= len(grid[0])
        min=0
        q= deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==2:
                    q.append((i,j,min))
        while len(q)>0:
                row, col, min = q.popleft()
                for r,c in [[-1,0], [1,0], [0,-1], [0,1]]:
                     nr= r+row
                     nc= c+col
                     if (nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1):
                          grid[nr][nc]= 2
                          q.append((nr, nc, min+1))
        for i in range(n):
             for j in range(m):
                  if(grid[i][j]==1):
                       return -1
        return min
