# https://www.geeksforgeeks.org/longest-sub-array-sum-k/

def sumK(arr, k):
    n = len(arr)
    sumMap = {}
    sum_=0
    maxLen = 0
    for i in range(n):
        sum_+=arr[i]
        if sum_==k:
            maxLen = i+1
        if sum_ not in sumMap:
            sumMap[sum_] = i

        if (sum_ - k) in sumMap:
            index = sumMap[sum_-k]
            if maxLen < i - index:
                maxLen = i - index

    return maxLen


if __name__=='__main__':
    arr = [10, 5, 2, 7, 1, 9]
    n = len(arr)
    k = 15
    print(sumK(arr,k))