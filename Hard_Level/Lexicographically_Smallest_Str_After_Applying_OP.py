class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        res = s

        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            res = min(res, curr)

            # Operation 1: add 'a' to digits at odd indices
            chars = list(curr)
            for i in range(1, len(s), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)
            if added not in visited:
                queue.append(added)

            # Operation 2: rotate by 'b'
            rotated = curr[-b:] + curr[:-b]
            if rotated not in visited:
                queue.append(rotated)

        return res
