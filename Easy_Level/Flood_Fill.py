class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]
        # If the original color is the same as new color
        if original == color:
            return image
        def dfs(r, c):
            # Check boundaries and matching color
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if image[r][c] != original:
                return
            # Fill the color
            image[r][c] = color
            # Visit neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        dfs(sr, sc)
        return image
