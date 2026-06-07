# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Store value -> index mapping
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        # Start from last element of postorder
        self.post_index = len(postorder) - 1
        def helper(left, right):
            if left > right:
                return None
            # Current root
            root_val = postorder[self.post_index]
            self.post_index -= 1
            root = TreeNode(root_val)
            # Find root in inorder
            mid = inorder_map[root_val]
            # Build right subtree first
            root.right = helper(mid + 1, right)
            # Build left subtree
            root.left = helper(left, mid - 1)
            return root
        return helper(0, len(inorder) - 1)
