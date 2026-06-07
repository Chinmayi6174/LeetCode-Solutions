class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = Counter(sub)
            
            # Sort by (-frequency, -value)
            sorted_items = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            
            # Keep top x elements
            top_x = {num for num, _ in sorted_items[:x]}
            
            # Sum elements that are among top x
            total = sum(num for num in sub if num in top_x)
            result.append(total)
        
        return result
