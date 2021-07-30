import random
import heapq
from sys import maxsize


class Node:
    def __init__(self, val, x, y):
        self.key = val
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.key < other.key

    def getKey(self):
        return self.key

    def getPos(self):
        return self.x, self.y


class Heap:
    def __init__(self, bucket):
        self.heap = bucket
        heapq.heapify(self.heap)

    def push(self, item: Node):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]


def kthSmallest(matrix, n: int, k: int) -> int:
    hp = Heap([Node(matrix[0][i], 0, i) for i in range(n)])
    ans = hp.top().getKey()
    while k:
        node = hp.pop()
        ans = node.getKey()
        x, y = node.getPos()
        if 0 <= x + 1 < n:
            hp.push(Node(matrix[x + 1][y], x + 1, y))
        else:
            hp.push(Node(maxsize, x + 1, y))
        k -= 1
    return ans


if __name__ == '__main__':
    n = 5
    matrix = [[0] * n for _ in range(n)]
    matrix[0][0] = random.randint(1, 100)
    for i in range(1, n):
        matrix[0][i] = random.randint(0, 5) + matrix[0][i - 1]
    for i in range(1, n):
        matrix[i][0] = random.randint(0, 5) + matrix[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] = random.randint(1, 100) + max(matrix[i][j - 1], matrix[i - 1][j])

    for row in matrix:
        print(*row, sep='\t\t')

    for k in range(1, n * n + 1):
        print('k: ', k, kthSmallest(matrix, len(matrix), k), sep=' ')
