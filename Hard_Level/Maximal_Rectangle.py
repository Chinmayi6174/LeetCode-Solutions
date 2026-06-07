class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0
        for row in matrix:
            # Update heights
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            # Compute largest rectangle in histogram
            max_area = max(max_area, self.largestRectangleArea(heights))
        return max_area
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        heights.pop()  # Restore
        return max_area
