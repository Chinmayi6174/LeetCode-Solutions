class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        first = 1  # ways to climb 1 step
        second = 2  # ways to climb 2 steps
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        return second
