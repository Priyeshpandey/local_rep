#

def merge(arr1, arr2) -> "O(m*n)":
    m, n = len(arr1), len(arr2)
    # arr1 will have first n elements in sorted sequence and arr2 will have last m
    for i in range(n - 1, -1, -1):
        last = arr1[m - 1]
        j = m - 2

        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1

        if j != m - 2 or last > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = last


def mergeFast(arr1, arr2):
    n, m = len(arr1), len(arr2)
    i, j, k = 0, 0, n - 1
    while i < k:
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr1[k], arr2[j] = arr2[j], arr1[k]
            j += 1
            k -= 1
    print(arr1)
    print(arr2)
    arr1.sort()
    arr2.sort()


if __name__ == '__main__':
    arr1 = [6, 7, 53, 84]
    arr2 = [2, 4, 36, 57, 70]
    mergeFast(arr1, arr2)
    print(arr1)
    print(arr2)
