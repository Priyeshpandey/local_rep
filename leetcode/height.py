#https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1#
import random
from sys import maxsize


def getMinDiff(arr, n, k):
    # code here
    arr.sort()
    res = arr[n-1] - arr[0]
    for i in range(1, n):
        small = min(arr[0]+k, arr[i]-k)
        big = max(arr[n-1]-k, arr[i-1]+k)
        if small < 0: continue
        res = min(res, big-small)

    return res


if __name__ == '__main__':
    n = 10
    k = 5
    target = "8 1 5 4 7 5 7 9 4 6"
    towerList = list(map(int, target.split()))
    # towerList = [random.randint(1, 20) for _ in range(n)]
    print(k)
    print(n)
    print(*towerList)
    print(getMinDiff(towerList, n, k))
