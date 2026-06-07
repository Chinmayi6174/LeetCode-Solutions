class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of both arrays
        i = m - 1  # Last element in nums1's actual data
        j = n - 1  # Last element in nums2
        k = m + n - 1  # Last index in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements left in nums2, place them in nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
