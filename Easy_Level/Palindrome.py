class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return x_str == x_str[::-1]
sol = Solution()
number=0
print(sol.isPalindrome(number))
