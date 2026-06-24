# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    def serialize(self, root):
        vals = []
        def preorder(node):
            if not node:
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ",".join(vals)
    def deserialize(self, data):
        if not data:
            return None
        preorder = list(map(int, data.split(",")))
        self.idx = 0
        def build(low, high):
            if self.idx == len(preorder):
                return None
            val = preorder[self.idx]
            if val < low or val > high:
                return None
            self.idx += 1
            node = TreeNode(val)
            node.left = build(low, val)
            node.right = build(val, high)
            return node
        return build(float("-inf"), float("inf"))
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
