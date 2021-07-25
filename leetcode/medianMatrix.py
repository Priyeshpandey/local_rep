# create min heap from first row with key=value_in_matrix, val = (x,y) position
# pop top of heap and push next element right below popped (x,y) that is (x+1,y) if x<n-1 else (1,y+1) if not seen
# else get next in col i.e (2,y+1) keep going until you find an element which is not seen already or reach till end
# if reach till end then put MAX, mark current selected as visited
# perform the above steps in sequence for size//2 times, on last iteration return the popped element
import heapq
from sys import maxsize
from random import randint


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


class Solution:
    '''
    1 2 3 7 9
    4 5 6 8 10
    7 8 9 10 12
    '''

    def median(self, matrix, r, c):
        col1 = [HeapNode(matrix[i][0], i, 0) for i in range(r)]
        hp = Heap(col1)
        mid = r * c // 2
        i = 0
        while i < mid:
            topNode = hp.pop()
            print(i,':',topNode.val)
            new_node = HeapNode(matrix[topNode.x][topNode.y + 1], topNode.x, topNode.y+1) if topNode.y < c - 1 else \
                HeapNode(maxsize, 0, 0)
            hp.push(new_node)
            i += 1

        return hp.pop().val


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


if __name__ == '__main__':
    row = 11
    col = 9
    # matrix = sorted_matrix_generator(1, row, col)
    string = "2 2 6 11 11 11 14 19 19 2 8 12 13 14 15 16 17 19 1 2 5 6 12 13 18 20 20 5 5 10 11 12 15 17 17 20 4 5 6 9 9 11 12 17 17 2 4 6 10 12 14 18 18 19 3 3 8 8 11 13 14 15 18 4 7 10 15 16 17 18 19 20 1 1 2 10 11 12 16 17 19 1 1 2 5 9 10 12 16 18 4 6 7 8 13 14 15 15 18"
    matrix = generate_matrix_from_string(string, row, col)
    for item in matrix:
        print(*item, sep='\t')
    sol = Solution()
    print(sol.median(matrix, row, col))
