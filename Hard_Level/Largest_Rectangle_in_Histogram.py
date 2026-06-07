class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # will store indices
        max_area = 0
        # Append a zero to flush remaining stack at the end
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # width calculation
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                max_area = max(max_area, height * width)
            stack.append(i)
        return max_area
