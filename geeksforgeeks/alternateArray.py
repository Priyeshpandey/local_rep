from typing import List


def modAlternate(arr: List[int]) -> None:
    n = len(arr)
    max_i, min_i = n - 1, 0
    i = 0
    me = arr[max_i] + 1
    while i < n:
        if i % 2 == 0:
            arr[i] += (arr[max_i] % me) * me
            max_i -= 1
        else:
            arr[i] += (arr[min_i] % me) * me
            min_i += 1
        i += 1

    for i in range(n):
        arr[i] = arr[i] // me

    print(arr)


def posNegAlternate(arr: List[int]) -> None:
    n = len(arr)
    i, j = 0, n - 1
    while i < j:
        if arr[i] < 0 and arr[j] > 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] < 0 and arr[j] < 0:
            j -= 1
        elif arr[i] > 0 and arr[j] > 0:
            i += 1
        else:
            i += 1
            j -= 1
    print(arr)

    i, j = 0, n - 1

    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 2
        j -= 1

    print(arr)


def rightRotate(arr, start, end):
    if start >= end or end >= len(arr):
        return
    temp = arr[end]
    for i in range(end, start, -1):
        arr[i] = arr[i - 1]
    arr[start] = temp


def orderAlternate(arr: List[int]) -> None:
    n = len(arr)
    i, j = 0, 1

    while i < n:
        if i % 2 == 0 and arr[i] > 0:
            while j < n and arr[j] > 0:
                j += 1
            rightRotate(arr, start=i, end=j)
            i += 2
            j = i + 1
        elif i % 2 == 1 and arr[i] < 0:
            while j < n and arr[j] < 0:
                j += 1
            rightRotate(arr, start=i, end=j)
            i += 2
            j = i + 1
        else:
            i += 1
    print(arr)


if __name__ == '__main__':
    arr = [4, -56, 2, 93, 8, -5, -6, 3, 4, 2, -8, 76]
    # arr.sort()
    # print(arr)
    # modAlternate(arr)
    # posNegAlternate(arr)
    orderAlternate(arr)
