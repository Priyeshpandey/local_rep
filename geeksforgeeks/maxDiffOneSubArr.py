def mdosa(arr):
    n = len(arr)
    start, end = 0, 1
    maxLen = 1

    while end < n:
        if abs(arr[end - 1] - arr[end]) <= 1:
            end += 1
        else:
            start = end
            end += 1

        if end - start > maxLen:
            maxLen = end - start

    return maxLen


def minDiff(arr1, arr2):
    arr1.sort()
    arr2.sort()
    n = len(arr1)
    m = len(arr2)

    i, j = 0, 0
    inf = float('inf')
    min_diff = inf
    while i < n and j < m:
        diff = abs(arr1[i] - arr2[j])
        if diff < min_diff:
            min_diff = diff
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return min_diff


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 10, 11, 12]
    arr2 = [100, 20, 30, 40, 15, 16, 18]
    # print(mdosa(arr))
    print(minDiff(arr,arr2))
