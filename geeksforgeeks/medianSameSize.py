def findMedian(arr1, arr2, n):  # O(n) Time O(1) Space
    i, j = 0, 0
    m1, m2 = -1, -1
    count = 0
    while count <= n:
        count += 1

        # case 1 if arr1[-1]<arr2[0]
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        elif j == n:
            m1 = m2
            m2 = arr1[0]
            break

        if arr1[i] <= arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m2 + m1) / 2


def findMedian2(arr1, arr2, n):  # O(log(N)) time, O(n) space
    if n == 0:
        return -1
    if n == 1:
        return (arr1[0] + arr2[0]) / 2
    if n == 2:
        return (min(arr1[1], arr2[1]) + max(arr1[0], arr2[0])) / 2

    m1 = arr1[n // 2] if n % 2 else (arr1[n // 2] + arr1[n // 2 - 1]) / 2
    m2 = arr2[n // 2] if n % 2 else (arr2[n // 2] + arr2[n // 2 - 1]) / 2

    if m1 == m2:
        return m1
    elif m1 > m2:
        if n % 2 == 0:
            return findMedian(arr1[int(n / 2 - 1):],
                              arr2[:int(n / 2 + 1)], int(n / 2) + 1)
        return findMedian(arr1[:int(n / 2) + 1],
                          arr2[int(n / 2):], int(n / 2) + 1)
    else:
        if n % 2 == 0:
            return findMedian(arr1[int(n / 2 - 1):],
                              arr2[:int(n / 2 + 1)], int(n / 2) + 1)
        else:
            return findMedian(arr1[int(n / 2):],
                              arr2[0:int(n / 2) + 1], int(n / 2) + 1)


def median(xL, xR, yL, yR, n1, n2):
    if (n1 + n2) % 2 == 0:
        return (max(xL, yL) + min(yR, xR)) / 2
    return max(yL, xL)


def findMedian3(arr1, arr2, n1, n2):
    if n1 > n2:
        return findMedian3(arr2, arr1, n2, n1)

    # At this point we are sure that n1<=n2
    # [1,2,3] x=3//2 =>1; y=(n1+n2)//2 - x
    #    ^
    # [4,5,6,7,8,9,10]
    #          ^
    # Find pivot in arr1
    inf = 100000
    mid = (n1 + n2 + 1) // 2
    start = 0
    end = n1
    while start <= end:
        x = (start + end) // 2
        y = mid - x
        xL = arr1[x - 1] if x > 0 else -inf
        xR = arr1[x] if x < n1 else inf
        yL = arr2[y - 1] if y > 0 else -inf
        yR = arr2[y] if y < n2 else inf
        if xL <= yR and yL <= xR:
            return median(xL, xR, yL, yR, n1, n2)
        elif xL > yR:
            end = x - 1
        else:
            start = x + 1
    raise Exception('Illegal input!!')


if __name__ == '__main__':
    arr1 = [1, 2, 8, 9, 11, 12, 15]  # 5
    arr2 = [3]  # 6.5
    # 1,2,3,6,7,8,8,9,10,12
    n1, n2 = len(arr1), len(arr2)
    Z = arr1 + arr2
    Z.sort()
    print(Z)
    zx = Z[(n1 + n2) // 2] if (n1 + n2) % 2 == 1 else (Z[(n1 + n2) // 2] + Z[(n1 + n2) // 2 - 1]) / 2
    x = findMedian3(arr1, arr2, n1, n2)
    assert x == zx, f'Mismatch (x){x}!=(zx){zx}'
    print(x)
