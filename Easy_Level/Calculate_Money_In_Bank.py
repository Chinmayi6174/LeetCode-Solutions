class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        # Sum for all complete weeks
        total = 0
        for i in range(weeks):
            # Each week starts with (1 + i) dollars on Monday
            total += sum((1 + i + d) for d in range(7))
        # Add remaining days
        total += sum((1 + weeks + d) for d in range(days))
        return total
