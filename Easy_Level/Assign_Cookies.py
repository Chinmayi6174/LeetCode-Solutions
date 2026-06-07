class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both greed factors and cookie sizes
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        # Try to satisfy children with the smallest possible cookie
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1  # child is satisfied
            cookie += 1  # move to next cookie
        return child
