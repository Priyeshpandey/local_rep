import heapq
import random


class Solution:
    def kthSmallest(self, arr, l, r, k):
        heapq.heapify(arr)
        kth = -1
        i = 0
        while i < k:
            kth = heapq.heappop()
            i += 1

        return kth


def separate(arr):
    n = len(arr)
    i = 0
    j = n - 1

    while i < j:
        if (arr[i] > 0) and arr[j] > 0:
            j -= 1
        elif (arr[i] < 0) and arr[j] > 0:
            i += 1
            j -= 1
        elif (arr[i] > 0) and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            i += 1

    return arr


class Sol:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0

    def update_col_bound(self, left, right):
        self.left = left
        self.right = right

    def update_row_bound(self, up, down):
        self.up = up
        self.down = down

    def update_bounds(self):
        if not self.up == self.down:
            self.update_row_bound(self.up + 1, self.down - 1)
        if not self.left == self.right:
            self.update_col_bound(self.left + 1, self.right - 1)

    def spiralPrint(self, matrix, r, c):
        if c == 1:
            for i in range(r):
                print(matrix[i][0], end=' ')
            return
        size = r * c
        x, y = 0, 0
        k = 0
        self.update_row_bound(0, r - 1)
        self.update_col_bound(0, c - 1)
        while k < size:
            print(matrix[x][y], end=' ')
            if x == self.up + 1 and y == self.left:
                self.update_bounds()

            if x == self.up and y < self.right:
                y += 1
            elif y == self.right and x < self.down:
                x += 1
            elif x == self.down and y > self.left:
                y -= 1
            elif y == self.left and x > self.up:
                x -= 1

            k += 1


def spiralPrint(matrix):
    n = len(matrix)
    m = len(matrix[0])
    col_start = 0
    col_end = m - 1
    row_start = 0
    row_end = n - 1

    k = 0
    result = []
    while k < n * m:
        # row: left-right
        result.extend(matrix[row_start][col_start:col_end + 1])
        k += col_end - col_start + 1
        row_start += 1

        # col: up-down
        if k < n * m:
            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            k += row_end - row_start + 1
            col_end -= 1
        else:
            break

        # row: right-left
        if k < n * m:
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][i])
            k += col_end - col_start + 1
            row_end -= 1
        else:
            break

        # col: down-up
        if k < n * m:
            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[i][col_start])

            k += row_end - row_start + 1
            col_start += 1

    return result


if __name__ == '__main__':
    n = 10
    m = 5

    matrix = [[random.randint(5, 20) for _ in range(m)] for _ in range(n)]
    for row in matrix:
        print(*row, sep='\t\t')

    result = spiralPrint(matrix)
    print(result)
