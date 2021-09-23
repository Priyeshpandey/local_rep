# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/
import sys


def stockSell2DP(stock):
    n = len(stock)
    dp = [0] * n
    max_r, min_l = stock[-1], stock[0]

    for i in range(n - 2, -1, -1):
        max_r = max(max_r, stock[i])
        dp[i] = max(dp[i + 1], max_r - stock[i])

    for i in range(1, n):
        min_l = min(min_l, stock[i])
        dp[i] = max(dp[i - 1], dp[i] + stock[i] - min_l)

    return dp[n - 1]


def stockSellEasy(stock):   #O(N) time and O(1) space
    n = len(stock)

    buy1, buy2 = sys.maxsize, sys.maxsize
    profit1, profit2 = 0, 0
    for i in range(n):
        buy1 = min(buy1, stock[i])
        profit1 = max(profit1, stock[i] - buy1)

        buy2 = min(buy2, stock[i] - profit1)
        profit2 = max(profit2, stock[i] - buy2)

    return profit2


if __name__ == '__main__':
    stocks = [3, 8, 97, 69, 823, 71, 6, 5, 2, 30, 60, 32, 9, 8, 6, 4, 9, 8, 2]
    print(stockSell2DP(stocks))
    print(stockSellEasy(stocks))
