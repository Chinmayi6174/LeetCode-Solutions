class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        n=len(s)
        freq={}
        for ch in t:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        l=0
        ml=float('inf')
        st=0
        ct=0
        for r in range(n):
            if s[r] in freq:
                if freq[s[r]]>0:
                    ct+=1
                freq[s[r]]-=1
            else:
                freq[s[r]]=-1
            ml=max(ml,freq[s[r]])
            while ct==len(t):
                if (r-l+1)<ml:
                    ml=r-l+1
                    st=l
                freq[s[l]]+=1
                if freq[s[l]]>0:
                    ct-=1
                l+=1
        if ml==float('inf'):
            return ""
        else:
            return s[st:st+ml]  
