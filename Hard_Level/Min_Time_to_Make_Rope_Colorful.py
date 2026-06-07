class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        n = len(colors)
        
        # Iterate through balloons
        for i in range(1, n):
            # If two consecutive balloons have the same color
            if colors[i] == colors[i - 1]:
                # Remove the one with smaller neededTime
                total_time += min(neededTime[i], neededTime[i - 1])
                # Keep the larger time for future comparisons
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        
        return total_time
