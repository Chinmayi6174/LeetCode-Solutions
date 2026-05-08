class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1  # shift left and set next bit to 1
        return x
