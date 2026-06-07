class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        # Mark walls and guards
        for r, c in walls:
            grid[r][c] = 1  # wall
        for r, c in guards:
            grid[r][c] = 2  # guard
        # Row-wise sweep (left→right, right→left)
        for r in range(m):
            seen = False
            for c in range(n):
                if grid[r][c] == 1:  # wall
                    seen = False
                elif grid[r][c] == 2:  # guard
                    seen = True
                elif seen:
                    grid[r][c] = 3  # guarded
            seen = False
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen:
                    grid[r][c] = 3
        # Column-wise sweep (top→bottom, bottom→top)
        for c in range(n):
            seen = False
            for r in range(m):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen:
                    grid[r][c] = 3
            seen = False
            for r in range(m - 1, -1, -1):
                if grid[r][c] == 1:
                    seen = False
                elif grid[r][c] == 2:
                    seen = True
                elif seen:
                    grid[r][c] = 3
        # Count unguarded (0) cells
        return sum(grid[r][c] == 0 for r in range(m) for c in range(n))
