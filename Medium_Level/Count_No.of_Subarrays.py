class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            count = 0
            odd = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd += 1
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                count += right - left + 1
            return count
        return atMost(k) - atMost(k - 1)

#another approach
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum=0
        count= {0:1}
        ans=0
        for num in nums:
            if num%2==1:
                prefix_sum+=1
            if prefix_sum -k in count:
                ans+= count[prefix_sum-k]
            if prefix_sum in count:
                count[prefix_sum]+=1
            else:
                count[prefix_sum]=1
        return ans
