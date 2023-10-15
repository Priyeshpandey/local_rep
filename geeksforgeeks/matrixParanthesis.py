import sys


def matrixMultiplication(N, matrix):
    # code here
    dp = [[0] * N for _ in range(N)]

    def minCost(dim, l, r):
        if l == r:
            return 0

        if dp[l][r]:
            return dp[l][r]

        min_ = sys.maxsize

        for k in range(l, r):
            count = minCost(dim, l, k) + minCost(dim, k + 1, r) + (dim[l - 1] * dim[k] * dim[r])
            min_ = count if count < min_ else min_
        dp[l][r] = min_
        return min_

    return minCost(matrix, 1, N - 1)


def matrixDP(mat):
    N = len(mat)
    dp = [[0] * N for _ in range(N)]

    for L in range(2, N):
        for l in range(1, N-L+1):
            r = l + L-1
            dp[l][r] = sys.maxsize
            for k in range(l, r):
                dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r] + mat[l - 1] * mat[k] * mat[r])
    # print(dp)
    return dp[1][N - 1]


if __name__ == '__main__':
    matrix = [40, 20, 30, 10, 30]
    print(matrixDP(matrix))
