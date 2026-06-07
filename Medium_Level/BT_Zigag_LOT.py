# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root==None):
            return []
        q=deque([root])
        ans=[]
        level_no=0
        while(len(q)>0):
            level=[]
            for _ in range(len(q)):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                level.append(node.val)
            if(level_no%2==1):
                ans.append(level[::-1])
            else:
                ans.append(level)
            level_no+=1
        return ans
