class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_count = Counter(num % value for num in nums)
        i = 0
        while True:
            if mod_count[i % value] > 0:
                mod_count[i % value] -= 1
                i += 1
            else:
                return i
