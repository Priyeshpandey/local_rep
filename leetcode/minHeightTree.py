from collections import deque


class Solution:
    def __init__(self):
        self.graph = {}

    def dfs(self, node, visited, bucket):
        visited[node] = 1
        bucket.append(node)
        neighbors = self.graph[node]
        max_height = 0
        max_bucket = []
        for ne in neighbors:
            if not visited[ne]:
                height, new_bucket = self.dfs(ne, visited, [])
                if height > max_height:
                    max_height = height
                    max_bucket = new_bucket
        bucket.extend(max_bucket)
        return 1 + max_height, bucket

    def findMinHeightTrees(self, n: int, edges):
        if len(edges) == 0:
            return [0]
        self.graph = {key: set() for key in range(n)}
        for edge in edges:
            a, b = edge
            self.graph[a].add(b)
            self.graph[b].add(a)

        leaf = -1
        for key in self.graph:
            if len(self.graph[key]) == 1:
                leaf = key
                break
        visited = [0 for _ in range(n)]
        height, bucket = self.dfs(leaf, visited, [])

        if len(bucket) % 2:
            return [bucket[len(bucket) // 2]]
        else:
            return bucket[len(bucket) // 2 - 1:len(bucket) // 2 + 1]


class Sol2:

    def findMinHeightTrees(self, n: int, edges):
        if len(edges) == 0:
            return [0]
        graph = {key: set() for key in range(n)}
        for edge in edges:
            a, b = edge
            graph[a].add(b)
            graph[b].add(a)

        q = []
        for i in range(n):
            if len(graph[i]) == 1:
                q.append(i)

        while len(graph) > 2:
            new_q = []
            for leaf in q:
                new_node = graph[leaf].pop()
                graph[new_node].remove(leaf)
                graph.pop(leaf)
                if len(graph[new_node]) == 1:
                    new_q.append(new_node)
            q = new_q

        return q


if __name__=='__main__':
    sol = Sol2()
    n = 3
    edges = [[0,1],[1,2]]
    print(sol.findMinHeightTrees(n,edges))