# https://practice.geeksforgeeks.org/problems/find-the-string-in-grid0111/1
from sortedcontainers import sortedset


class Solution:
    def __init__(self):
        self.dir = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        self.R = 0
        self.C = 0
        self.k = 0

    def searchWord(self, grid, word):
        n, m = len(grid), len(grid[0])
        k = len(word)

        self.R = n
        self.C = m
        self.k = k
        count = sortedset.SortedSet()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == word[0]:
                    for dx, dy in self.dir:
                        if self.countWord(i, j, dx, dy, word, grid):
                            count.add((i, j))

        return count

    def countWord(self, i, j, dx, dy, word, grid):
        match = 1
        x, y = i, j
        for k in range(1, self.k):
            x, y = x + dx, y + dy
            if 0 <= x < self.R and 0 <= y < self.C:
                if grid[x][y] != word[k]:
                    match = 0
                    break
            else:
                match = 0
                break

        return match


if __name__ == '__main__':
    grid = ['paaka',
            'pacap',
            'aacaa',
            'packa',
            'akaka']

    word = 'pack'
    sol = Solution()
    print(sol.searchWord(grid, word))
