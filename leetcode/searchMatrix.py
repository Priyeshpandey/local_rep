from typing import List
from random import randint


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    size = n * m
    lo = 0
    hi = size - 1

    while lo <= hi:
        mid = lo + (hi - lo) // 2
        x, y = mid // m, mid % m
        print('hi,lo,mid : ',hi, lo, mid)
        print('x,y :',x,y)
        if matrix[x][y] == target:
            return True
        if matrix[x][y] < target:
            lo = mid+1
        else:
            hi = mid-1
    return False


class Solution:
    pass



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

if __name__ == '__main__':
    matrix = sorted_matrix_generator(10,4,3)
    # matrix = [[10, 13, 17], [19, 22, 23], [25, 29, 30], [34, 36, 38]]
    for row in matrix:
        print(row)
    print(searchMatrix(matrix, 25))