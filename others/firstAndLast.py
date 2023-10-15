import bisect


def find(arr, n, x):
    # code here
    lo = bisect.bisect_left(arr, x, 0, n - 1)
    hi = bisect.bisect_right(arr, x, 0, n - 1)
    if arr[lo] == x:
        if arr[hi] == x:
            return lo, hi
        if arr[hi-1]==x:
            return lo, hi-1

    return -1, -1


if __name__ == '__main__':
    arr = [5]
    x = 5
    print(find(arr, len(arr), x))
