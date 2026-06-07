from collections import deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        q = deque([(beginWord, 1)])
        # mark beginWord visited if present
        if beginWord in wordset:
            wordset.remove(beginWord)
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i+1:]
                    if new_word in wordset:
                        q.append((new_word, steps + 1))
                        wordset.remove(new_word)
        return 0
