from typing import List

'''
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
'''


class Solution:
    def __init__(self):
        self.graph = {}
        self.status = []
        self.result = []
        self.UNVISITED, self.EXPLORING, self.DONE = 0, 1, 2

    def findOrder(self, n: int, pq: List[List[int]]) -> List[int]:
        self.status = [self.UNVISITED for _ in range(n)]

        for x, y in pq:
            if y not in self.graph:
                self.graph[y] = [x]
            else:
                self.graph[y].append(x)
        hasCycle = self.hasCycle(n)
        self.result.reverse()
        return self.result if not hasCycle else []

    def hasCycle(self, n):
        for node in range(n):
            if self.status[node] == self.UNVISITED and self.dfs(node):
                return True

        return False

    def dfs(self, node):
        if node not in self.graph:
            self.result.append(node)
            self.status[node] = self.DONE
            return False

        if self.status[node] == self.EXPLORING:
            return True

        if self.status[node] == self.DONE:
            return False

        self.status[node] = self.EXPLORING

        for ne in self.graph[node]:
            if self.status[ne] == self.UNVISITED and self.dfs(ne):
                return True
        self.status[node] = self.DONE
        self.result.append(node)

        return False
