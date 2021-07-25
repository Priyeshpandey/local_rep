# TODO: Find efficient approach

from typing import List
import random
import pprint
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        print(f"Time elapsed : {time.time() - start}")
        return res

    return wrapper

class Solution:
    def __init__(self):
        self.cum_sum = None

    def set_cum_sum_row_wise(self, matrix):
        n = len(matrix)
        self.cum_sum = []
        for i in range(n):
            row = []
            cum_sum=0
            for num in matrix[i]:
                cum_sum+=num
                row.append(cum_sum)
            self.cum_sum.append(row)

    def get_sum(self, row_start, row_end, col_start, col_end):
        return 0
        sum_ = 0
        for row in range(row_start, row_end+1):
            sum_ += self.cum_sum[row][col_end] - (self.cum_sum[row][col_start-1] if col_start > 0 else 0)
        return sum_

    @timer
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        steps = 0
        max_sum = -100*10000
        rows = len(matrix)
        cols = len(matrix[0])
        self.set_cum_sum_row_wise(matrix)
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        calc_sum = self.get_sum(row_start, row_end, col_start, col_end)
                        if calc_sum <= k:
                            max_sum = max(max_sum, calc_sum)
                        steps += 1
        # print(steps)
        return max_sum


def matrix_print(matrix):
    rows = len(matrix)
    print(*[matrix[i] for i in range(rows)], sep='\n')


if __name__ == '__main__':
    rows, cols = 100, 100
    k = 30
    matrix = [[random.randint(-10, 10) for _ in range(cols)] for i in range(rows)]
    # matrix = [[2, 2, -1]]
    matrix_print(matrix)
    sol = Solution()
    print(sol.maxSumSubmatrix(matrix, k))
