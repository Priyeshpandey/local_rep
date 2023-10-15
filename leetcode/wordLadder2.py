# https://leetcode.com/problems/word-ladder-ii/
from copy import deepcopy
from typing import List, Optional
from collections import deque


class Solution:
    def __init__(self):
        self.res = []

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        wordSet = set(wordList)
        visited = {}
        adj_list = {}
        q = deque()
        q.append(beginWord)
        visited[beginWord] = 0
        while q:
            curr_word = q.popleft()
            aux_curr_word = [w for w in curr_word]
            # print(aux_curr_word)
            for i in range(len(aux_curr_word)):
                temp = aux_curr_word[i]
                for j in range(ord('a'), ord('z') + 1):
                    if chr(j) == temp:
                        continue
                    aux_curr_word[i] = chr(j)
                    processed_curr_word = ''.join(aux_curr_word)
                    if processed_curr_word in wordSet:
                        # print(processed_curr_word)
                        if processed_curr_word not in visited:
                            visited[processed_curr_word] = visited[curr_word] + 1
                            q.append(processed_curr_word)
                            if curr_word in adj_list:
                                adj_list[curr_word].add(processed_curr_word)
                            else:
                                adj_list[curr_word] = {processed_curr_word}
                        elif processed_curr_word in visited and visited[processed_curr_word] == visited[curr_word]+1:
                            if curr_word in adj_list:
                                adj_list[curr_word].add(processed_curr_word)
                            else:
                                adj_list[curr_word] = {processed_curr_word}
                aux_curr_word[i] = temp
        # Here on all we need to do is using custom adj_list, do a DFS to find all possible paths
        # print(adj_list)
        # print(visited)
        path = []
        self.dfs(beginWord, endWord, adj_list, path)
        return self.res

    def dfs(self, beginWord, endWord, adj_list, path):
        path.append(beginWord)
        if beginWord == endWord:
            self.res.append(deepcopy(path))
            path.pop()
            return

        if beginWord in adj_list:
            for word in adj_list[beginWord]:
                self.dfs(word, endWord, adj_list, path)

        path.pop()





if __name__ == '__main__':
    """
    "a"
"c"
["a","b","c"]
    """
    beginWord = 'a'
    endWord = 'c'
    wordList = ["a","b","c"]
    sol = Solution()
    print(sol.findLadders(beginWord, endWord, wordList))
