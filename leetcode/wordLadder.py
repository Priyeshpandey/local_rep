# https://leetcode.com/problems/word-ladder/
from typing import List, Optional
from collections import deque


class Solution:
    def getNextWordList(self, src, wordSet) -> list:
        n = len(src)
        word = [x for x in src]
        nextWordList = []
        for i in range(n):
            for j in range(ord('a'), ord('z') + 1):
                temp = word[i]
                word[i] = chr(j)
                target = ''.join(word)
                if target in wordSet:
                    nextWordList.append(target)
                word[i] = temp
        return nextWordList

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque()
        q.append(beginWord)
        length = 0

        while q:
            length += 1
            qlen = len(q)
            for i in range(qlen):
                cur_word = q.popleft()
                next_word_list = self.getNextWordList(cur_word, wordSet)
                for next_word in next_word_list:
                    if next_word == endWord:
                        return length+1
                    q.append(next_word)
                    wordSet.remove(next_word)

        return 0


if __name__ == '__main__':
    beginWord = 'hit'
    endWord = 'cog'
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    print(sol.ladderLength(beginWord, endWord, wordList))
