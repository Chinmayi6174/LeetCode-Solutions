class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}   # stores last seen index
        left = 0
        max_len = 0
        for right in range(len(s)):
            if s[right] in char_index:
                left = max(left, char_index[s[right]] + 1) # Move left forward
            char_index[s[right]] = right
            max_len = max(max_len, right - left + 1)
        return max_len


#another approach
def lenoflongsubstr(self, s):
    n=len(s)
    left=0
    ml=0
    chset=set()
    for r in range(n):
        if s[r] not in chset:
            chset.add(s[r])
            ml=max(ml, r-left+1)
        else:
            ml=0
            left=0
            z=0
            for r in range(len(nums)):
                if nums[r]==0:
                    z+=1
                while z>k:
                    if nums[left]==0:
                        z-=1
                    left+=1
                ml=max(ml, r-left+1)
            return ml
