def nextPermutation(arr):
    n = len(arr)
    localMax = 0
    for i in range(n - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            localMax = i
            break
    base = localMax-1
    nextBig = localMax
    k = localMax
    if localMax > 0:
        while k < n:
            if arr[base] < arr[k] < arr[nextBig]:
                nextBig = k
            k += 1

        arr[base], arr[nextBig] = arr[nextBig], arr[base]

    i, j = localMax, n - 1
    # print(arr)
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    print(arr)


if __name__=='__main__':
    arr = [1,2,3,4,5]
    n = len(arr)
    # print(arr)
    for _ in range(120):
        nextPermutation(arr)