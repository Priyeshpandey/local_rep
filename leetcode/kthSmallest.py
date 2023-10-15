import copy
import random
import heapq
from sys import maxsize


class HeapNode:
    def __init__(self, node, X, Y):
        self.val = node
        self.x = X
        self.y = Y

    def getKey(self):
        return self.val

    def getVal(self):
        return self.x, self.y

    def __lt__(self, other):
        return self.getKey() < other.getKey()


class Heap:
    def __init__(self, arr):
        self.heap = arr
        self.heapify()

    def heapify(self):
        heapq.heapify(self.heap)

    def pop(self):
        return heapq.heappop(self.heap)

    def push(self, node):
        heapq.heappush(self.heap, node)

    def getTop(self):
        return self.heap[0]



class Sol:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        # 1. build heap for 1st row
        hp = Heap([HeapNode(matrix[0][y], 0, y) for y in range(n)])

        x, y = 0, 0
        for _ in range(k):
            top = hp.pop()
            x, y = top.getVal()
            new_node = matrix[x + 1][y] if x < n - 1 else maxsize
            hp.push(HeapNode(new_node, x+1, y))

        return matrix[x][y]


if __name__ == '__main__':
    # myList = [HeapNode(i, i + 1, i + 2) for i in range(10)]
    # heapq.heapify(myList)
    # print(*[item.getKey() for item in myList])
    # pass
    n = 5
    matrix = [[0] * n for _ in range(n)]
    # print(matrix)
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

    for k in range(1, n*n+1):
        sol = Sol()
        print('k: ', k, sol.kthSmallest(matrix, k), sep=' ')
