class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    right = mid - 1  # keep searching left
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return res
        def findRight():
            left, right = 0, len(nums) - 1
            res = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    res = mid
                    left = mid + 1  # keep searching right
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1  
            return res
        return [findLeft(), findRight()]
