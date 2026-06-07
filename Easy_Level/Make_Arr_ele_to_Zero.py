class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        def simulate(start, direction):
            arr = nums[:]  # copy
            curr = start
            dirn = direction
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dirn
                else:
                    arr[curr] -= 1
                    dirn *= -1  # reverse direction
                    curr += dirn
            return all(x == 0 for x in arr)
        count = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):   # move right
                    count += 1
                if simulate(i, -1):  # move left
                    count += 1
        return count
