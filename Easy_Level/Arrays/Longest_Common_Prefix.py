class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # Start by assuming the entire first string is the prefix
        prefix = strs[0]
        # Compare the prefix with every string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the beginning of s
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""
        return prefix
