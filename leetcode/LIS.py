# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3808/
from sys import maxsize
from bisect import bisect_right, bisect_left


def lis(arr):
    n = len(arr)
    LIS = [1] * n
    for i in range(n):
        for j in range(i):
            LIS[i] = max(LIS[i], (1 + LIS[j]) if arr[i] > arr[j] else 1)
        # print(LIS)

    # print(LIS)
    return max(LIS)


def lisFast(nums):
    n = len(nums)
    dp = [-maxsize] + [maxsize] * n
    for i in range(n):
        idx = bisect_right(dp, nums[i], 0, n)
        dp[idx] = nums[i]

    for i in range(n, 0, -1):
        if dp[i] != maxsize:
            return i


if __name__ == '__main__':
    arr = [10, 5, 8, 3, 9, 4,12,11]
    n = len(arr)
    print(arr)
    print(lisFast(arr))
