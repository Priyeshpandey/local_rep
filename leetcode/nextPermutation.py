import bisect
def nextPermutation(arr):
    n = len(arr)

    bP = 0

    for i in range(n - 1, 0, -1):
        if arr[i] > arr[i - 1]:
            bP = i
            break
    lastGreater = bP
    base = bP - 1
    if bP > 0:
        for i in range(bP, n):
            if arr[base] < arr[i] < arr[lastGreater]:
                lastGreater = i

        arr[lastGreater], arr[base] = arr[base], arr[lastGreater]

    i, j = bP, n - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def getCount(arr,x):
    n = len(arr)
    return bisect.bisect_right(arr,x,0,n-1) - bisect.bisect_left(arr,x,0,n-1)


if __name__ == '__main__':
    arr = [1,1,2,2,2,2,3]
    print(getCount(arr,3))
    # for i in range(24):
    #     nextPermutation(arr)
    #     print(arr)
