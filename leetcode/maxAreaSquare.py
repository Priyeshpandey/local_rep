# https://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/
from typing import List
from sortedcontainers import SortedList
from leetcode.custom_lib import binary_matrix_generator, printMatrix, generate_matrix_from_string


def max_area_square(inner_matrix: List[List[int]]) -> List[List[int]]:
    n, m = len(inner_matrix), len(inner_matrix[0])
    S: List[List[int]] = [[0]*m for _ in range(n)]
    max_pos: tuple[int, int] = 0, 0
    for i in range(n):
        S[i][0] = inner_matrix[i][0]
        max_pos = (i, 0) if S[i][0] > S[max_pos[0]][max_pos[1]] else max_pos

    for i in range(m):
        S[0][i] = inner_matrix[0][i]
        max_pos = (0, i) if S[0][i] > S[max_pos[0]][max_pos[1]] else max_pos

    for i in range(1,n):
        for j in range(1,m):
            if inner_matrix[i][j]:
                S[i][j] = min(S[i-1][j], S[i][j-1], S[i-1][j-1]) + 1
                max_pos = (i,j) if S[i][j] > S[max_pos[0]][max_pos[1]] else max_pos
            else:
                S[i][j] = 0

    fx, fy = max_pos
    max_val = S[fx][fy]
    print(fx,fy,max_val)
    return [[inner_matrix[i][j] for j in range(fy - max_val + 1, fy + 1)] for i in range(fx - max_val + 1, fx + 1)]


if __name__ == '__main__':
    r, c = 5, 4
    matrix = binary_matrix_generator(r, c)
    printMatrix(matrix)
    print("-" * 20)
    printMatrix(max_area_square(matrix))
