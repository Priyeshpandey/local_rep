######

def upper_bound(arr, x, lo, high):
    if x > arr[high]:
        return -1  # Upper bound does not exists
    if x == arr[high]:
        return high

    while lo < high:
        mid = (lo + high) // 2
        if x >= arr[mid]:
            lo = mid + 1
        else:
            high = mid

    return lo if arr[lo] >= x else lo + 1


def lower_bound(arr, x, lo, high):
    if x < arr[lo]:
        return -1  # Lower bound does not exists
    if x == arr[lo]:
        return lo

    while lo < high:
        mid = (lo + high) // 2
        if x <= arr[mid]:
            high = mid
        else:
            lo = mid + 1

    return lo if arr[lo] <= x else lo - 1


n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
n1 = len(arr1)
arr1 = [(arr1[i], i) for i in range(n1)]
arr1.sort()  # sort -> n1log(n1)

arr2 = list(map(int, input().split()))
n2 = len(arr2)
arr2 = [(arr2[i], i) for i in range(n2)]
arr2.sort()  # sort -> n2log(n2)
my_set = {}  # Global


def add2set(arr1, arr2, n1, n2):  # O(n1*log(n2))
    aux_arr2 = [ele[0] for ele in arr2]
    for i in range(n1):  # O(n1)
        up = upper_bound(aux_arr2, arr1[i][0], 0, n2 - 1)  # log(n2)
        sum_up = (arr1[i][0] + aux_arr2[up]) if up > -1 else 0  # O(1)
        lo = lower_bound(aux_arr2, arr1[i][0], 0, n2 - 1)  # log(n2)
        sum_lo = (arr1[i][0] + aux_arr2[lo]) if lo > -1 else 0
        if sum_up > 0 and sum_up not in my_set:  # O(1) or log(|my_set|)
            my_set[sum_up] = (arr1[i][1], arr2[up][1])  # O(1)

        if sum_lo > 0 and sum_lo not in my_set:  # O(log(|my_set|)
            my_set[sum_lo] = (arr1[i][1], arr2[lo][1])

try:
    add2set(arr1, arr2, n1, n2)
    add2set(arr2, arr1, n2, n1)
except MemoryError as e:
    pass

output = list(my_set.values())

for i in range(n1 + n2 - 1):
    print(*output[i])
