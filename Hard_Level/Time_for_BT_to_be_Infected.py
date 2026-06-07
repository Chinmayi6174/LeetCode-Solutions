# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
         # Build graph from tree
        graph = {}
        def build(node, parent):
            if not node:
                return
            if node.val not in graph:
                graph[node.val] = []
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            build(node.left, node)
            build(node.right, node)
        build(root, None)
        # BFS infection spread
        q = deque([(start, 0)])
        visited = set([start])
        time = 0
        while q:
            node, t = q.popleft()
            time = max(time, t)
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, t + 1))
        return time
