# https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1

def countPS(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    for L in range(1, n + 1):
        for start in range(n):
            end = start+L-1
            if end >= n:
                break

            if start == end:
                dp[start][end] = 1
            elif arr[start] == arr[end]:
                dp[start][end] = 1 + dp[start + 1][end] + dp[start][end - 1]
            else:
                dp[start][end] = dp[start + 1][end] + dp[start][end - 1] - dp[start + 1][end - 1]

    return dp[0][n - 1]


if __name__ == '__main__':
    print(countPS('ababa'))
