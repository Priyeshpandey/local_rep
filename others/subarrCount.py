# https://www.geeksforgeeks.org/count-of-subarrays-with-largest-element-at-least-twice-the-largest-of-remaining-elements/

def subarrCount(arr):
    n = len(arr)
    max_ = max(arr)
    i, j = 0, n-1
    count = 0
    for i in range(n):
        if arr[i] < max_//2:
            count+=1
        else:
            break

    for j in range(n):
        if arr[n-j-1] < max_//2:
            count+=1
        else:
            break

    return i*(n-j-1)


if __name__=='__main__':
    arr = [1, 6, 10, 9, 7, 3]
    print(subarrCount(arr))