class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ps=0
        freq= {0:1}
        ans=0
        for num in nums:
            ps+=num
            if ps-goal in freq:
                ans+=freq[ps-goal]
            if ps in freq:
                freq[ps]+=1
            else:
                freq[ps]=1
        return ans
