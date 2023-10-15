from sys import maxsize
import random


def kadaneAlgo(arr):
    n = len(arr)

    run_sum = 0
    max_sum = -maxsize
    start = 0
    end = 0
    for i in range(n):
        run_sum += arr[i]

        if run_sum > max_sum:
            max_sum = run_sum
            end = i

        if run_sum < 0:
            run_sum = 0
            start = i + 1
    print(start, end)
    return max_sum


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


if __name__ == '__main__':
    # n = 10
    # arr = [random.randint(-5, 10) for _ in range(n)]
    arr = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print(arr)
    print(maxSubArraySum(arr, len(arr)))
