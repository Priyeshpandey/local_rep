def alternateSort(arr):
    n = len(arr)
    arr.sort()
    i, j = 1, 1

    while j < n:
        if arr[j] > 0:
            break
        j += 1

    while (arr[i] < 0) and (j < n):
        arr[i], arr[j] = arr[j], arr[i]

        i += 2
        j += 1

    return arr


if __name__ == '__main__':
    arr = [4, -9, 7, -6, 5, -17, 40, -1, 4]
    print(alternateSort(arr))
