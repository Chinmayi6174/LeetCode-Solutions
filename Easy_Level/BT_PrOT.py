# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
      
#another approach
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack= [root]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
      
#another approach
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        curr=root
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr= curr.right
            else:
                pred= curr.left
                while pred.right and pred.right!= curr:
                    pred= pred.right
                if not pred.right:
                    res.append(curr.val)
                    pred.right=curr
                    curr= curr.left
                else:
                    pred.right=None
                    curr=curr.right
        return res
