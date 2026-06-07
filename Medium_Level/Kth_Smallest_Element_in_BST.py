# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=0
        c=0
        def inorder(root):
            nonlocal c
            nonlocal res
            if root:
                inorder(root.left)
                c+=1
                if c==k:
                    res=root.val
                inorder(root.right)
        inorder(root)
        return res
