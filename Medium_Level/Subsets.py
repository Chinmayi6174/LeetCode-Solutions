class Solution:
    def subsets (self, nums: List[int])->List[List[int]]:
        res=[]
        n= len(nums)
        for i in range(1<<n):
            s=[]
            for j in range(n):
                if i&(1<<j):
                    s.append(nums[j])
            res.append(s)     
        return res
nums=[1,7,4]        
print("subsets(nums)")
