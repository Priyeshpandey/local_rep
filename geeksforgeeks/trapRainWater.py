from typing import List


def trapWater(arr: List[int]) -> int:
    n = len(arr)
    left, right = [0] * n, [0] * n

    max_left, max_right = arr[0], arr[-1]

    for i in range(1, n):
        left[i] = max(max_left, arr[i - 1])
        max_left = max(max_left, left[i])

    for i in range(n - 2, -1, -1):
        right[i] = max(max_right, arr[i + 1])
        max_right = max(max_right, right[i])

    water = 0

    for i in range(1, n - 1):
        res = min(left[i], right[i]) - arr[i]
        print((i,res),end='| ')
        water += res if res > 0 else 0
    print('\n')
    print(left)
    print(right)
    return water


if __name__ == '__main__':
    arr = [6, 1, 8, 9, 2, 7, 9, 5, 4, 3]
    print(arr)
    print(trapWater(arr))
    #
    #
    # **#
    # **#
    # **#
    ##*#
    ##*#
    ##*#
    ##*#
    ####################
