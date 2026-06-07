class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # sqrt(0) = 0 and sqrt(1) = 1
        left, right = 2, x // 2  # No need to check beyond x//2 for x >= 2
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return right  # right is the integer part of sqrt(x)
