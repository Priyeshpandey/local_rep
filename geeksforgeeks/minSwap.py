# Minimum swaps required bring elements less equal K together

def minSwap(arr, n, k):
    bv, gv = 0, 0

    for i in range(n):
        if arr[i] <= k:
            gv += 1

    for i in range(gv):
        if arr[i] > k:
            bv += 1

    min_ = bv
    j = 0
    i = gv

    while i < n:
        min_ = min(min_, bv)
        if arr[j] > k:
            bv -= 1
        j += 1
        if arr[i] > k:
            bv += 1
        i += 1

    return min(min_, bv)


if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    k = int(input())

    print(arr, k)

    print(minSwap(arr,n,k))