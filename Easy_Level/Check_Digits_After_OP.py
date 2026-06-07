class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert string to list of integers
        digits = [int(ch) for ch in s]
        # Continue until only two digits remain
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits
        # Check if the final two digits are the same
        return digits[0] == digits[1]
