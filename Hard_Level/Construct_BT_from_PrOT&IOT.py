# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Store inorder value -> index
        inorder_map = {}
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        self.pre_index = 0

        def helper(left, right):
            if left > right:
                return None

            # Pick current root from preorder
            root_val = preorder[self.pre_index]
            self.pre_index += 1

            root = TreeNode(root_val)

            # Find root position in inorder
            mid = inorder_map[root_val]

            # Build left and right subtrees
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)
