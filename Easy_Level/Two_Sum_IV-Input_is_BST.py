# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def dfs(node):
            if not node:
                return False
            if (k - node.val) in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)

#anther approach
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(node, arr):
            if not node:
                return None
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)
        arr=[]
        inorder(root, arr)
        l=0
        r=len(arr)-1
        while l<r:
            s=arr[l]+arr[r]
            if s==k:
                return True
            elif s<k:
                l+=1
            else:
                r-=1
        return False
