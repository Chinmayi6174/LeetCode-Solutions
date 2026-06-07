class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # Create is_inc[i] = 1 if nums[i] < nums[i+1]
        is_inc = [0] * (n - 1)
        for i in range(n - 1):
            if nums[i] < nums[i + 1]:
                is_inc[i] = 1

        # Prefix sum to support fast range sum queries
        prefix = [0] * (n)
        for i in range(n - 1):
            prefix[i + 1] = prefix[i] + is_inc[i]

        # Helper to check if range [i, i + k - 2] is strictly increasing
        def is_strictly_increasing(start, k):
            return prefix[start + k - 1] - prefix[start] == k - 1

        # Binary search for the maximum k
        left, right = 1, n // 2
        ans = 0
        while left <= right:
            k = (left + right) // 2
            found = False
            for i in range(n - 2 * k + 1):
                if is_strictly_increasing(i, k) and is_strictly_increasing(i + k, k):
                    found = True
                    break
            if found:
                ans = k
                left = k + 1
            else:
                right = k - 1

        return ans
