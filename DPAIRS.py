######


n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr1 = [(arr1[i], i) for i in range(n)]
arr1.sort()  # sort -> nlog(n)

arr2 = list(map(int, input().split()))
arr2 = [(arr2[i], i) for i in range(m)]
arr2.sort()  # sort -> mlog(m)


def print_pairs(arr1, arr2, n, m):  # O(n+m)
    # my_set = {}
    for i in range(m):
        print(arr1[0][1], arr2[i][1])

    for i in range(1,n):
        print(arr1[i][1], arr2[m-1][1])

print_pairs(arr1, arr2, n, m)
#overall = O(n+m+nlogn+mlogm)