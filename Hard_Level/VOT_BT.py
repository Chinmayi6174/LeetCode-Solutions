# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque([(0,0,root)])
        d=defaultdict(lambda:defaultdict(list))
        while(len(q)>0):
            vertical,level,node=q.popleft()
            if(node.left):
                q.append((vertical-1,level+1,node.left))
            if(node.right):
                q.append((vertical+1,level+1,node.right))
            d[vertical][level].append(node.val)
        ans=[]
        for i in sorted(d):
            col=[]
            for j in sorted(d[i]):
                col.extend(sorted(d[i][j]))
            ans.append(col)
        return ans
