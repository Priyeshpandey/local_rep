def threeWayPartition(arr, a, b):
    print('range', a, b)
    # code here
    n = len(arr)
    p = 0
    i = 0
    while i < n:
        if arr[i] < a and i >= p:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
        else:
            i += 1

    i = p
    while i < n:
        if arr[i] < b and i>=p:
            arr[i], arr[p] = arr[p], arr[i]
            p += 1
        else:
            i += 1

    print(arr)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    a, b = map(int, input().split())
    print(arr)
    threeWayPartition(arr, a, b)
