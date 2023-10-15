
n, x, y = map(int, input().split())
contest = []
for _ in range(n):
    s, e = map(int, input().split())  # start,end times of contest
    contest.append((s, e))

V = list(map(int, input().split()))  # Times at which wormhole opens at house

W = list(map(int, input().split()))  # Times wormhole opens at exam centre

V.sort()
W.sort()



def get_lower_index(arr, target, start, end):
    if target > arr[end]:
        return end

    if target < arr[start]:
        return -1
    while start < end:
        # print('GLB--> ', start, end)
        mid = (start + end) // 2
        if target >= arr[mid]:
            start = mid + 1
        else:
            end = mid

    return start if arr[start] <= target else start-1


def get_upper_index(arr, target, start, end):
    if target > arr[end]:
        return -1
    if target < arr[start]:
        return start
    while start < end:
        # print('LUB--> ', start, end)
        mid = (end + start) // 2
        if target <= arr[mid]:
            end = mid
        else:
            start = mid + 1

    return start if arr[start] >= target else start+1


min_duration = 100000008

for i in range(n):
    start_of_contest = contest[i][0]
    end_of_contest = contest[i][1]
    v = get_lower_index(V, start_of_contest, 0, x-1)
    w = get_upper_index(W, end_of_contest, 0, y-1)
    if v==-1 or w==-1:
        continue
    else:
        if (W[w] - V[v]) < min_duration:
            min_duration = (W[w] - V[v])

print(min_duration+1)
