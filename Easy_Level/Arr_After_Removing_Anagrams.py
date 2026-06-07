class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]  # Always keep the first word
        for i in range(1, len(words)):
            # Compare sorted characters of current word and the last word in result
            if sorted(words[i]) != sorted(result[-1]):
                result.append(words[i])
        return result
