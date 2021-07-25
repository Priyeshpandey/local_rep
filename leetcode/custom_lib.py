from random import randint
from sys import maxsize
import time
import heapq


def sortedSquareMatrix(N, Mat):
    merge = []
    for row in Mat:
        merge += row
    merge.sort()
    for i in range(N):
        for j in range(N):
            Mat[i][j] = merge[i * N + j]
    return Mat


def sorted_matrix_generator(start, row, col):
    c = start
    n, m = row, col
    size = n * m
    fill = [0] * size
    fill[0] = c
    for i in range(1, size):
        fill[i] = fill[i - 1] + randint(1, 5)
    matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = fill[i * m + j]

    return matrix


def generate_matrix_from_string(string, n, m):
    fill = list(map(int, string.split()))
    matrix = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            matrix[i][j] = fill[i * m + j]

    return matrix


# Generates {<int>:(x,y)} type of nodes, comparison on basis of key
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


# Heap data structure of HeapNode
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


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Took {time.time() - start} s to finish {func.__name__}")

    return wrapper


def maxSubArraySum(a, size):
    max_so_far = -maxsize
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def binary_matrix_generator(r, c):
    matrix = [[randint(1, 3) % 2 for _ in range(c)] for _ in range(r)]
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(*row, sep='\t\t')


if __name__ == '__main__':
    printMatrix(binary_matrix_generator(5, 4))
