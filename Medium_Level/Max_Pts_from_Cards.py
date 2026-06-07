class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        winsize= n-k
        winsum= sum(cardPoints[:winsize])
        maxwinsize= winsum
        total= sum(cardPoints)
        for i in range(winsize,n):
            winsum += cardPoints[i]-cardPoints[i-winsize]
            maxwinsize= min(maxwinsize, winsum)
        return total-maxwinsize
