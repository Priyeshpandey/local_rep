import bisect


def bin_search(arr, hi, lo, target):  # returns index of the element in a sorted array if found else -1
    while hi > lo:
        mid = (hi + lo) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    return -1


def upper_bound(arr, hi, lo, target):
    while hi > lo:
        mid = (hi + lo) // 2
        if target >= arr[mid]:
            lo = mid + 1
        else:
            hi = mid
    # print(f"DBG--> {hi}---{lo}")
    return hi if arr[hi] >= target and hi < len(arr) else hi + 1


def lower_bound(arr, hi, lo, target):
    while hi > lo:
        mid = (hi + lo) // 2
        if target <= arr[mid]:
            hi = mid
        else:
            lo = mid + 1
    # print(f"DBG--> {hi}---{lo}")
    return hi if arr[hi] <= target and hi > 0 else hi - 1


def expo_search(arr, x, hi, lo):
    if arr[lo] == x:
        return lo

    i = 1
    while i < hi and arr[i] < x:
        i = 2 * i

    return bin_search(arr, min(i, hi), i // 2, x)


def bub_sort(arr, n):
    for i in range(n):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


def sel_sort(arr, n):
    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def merge2(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, lo, hi):
    if lo < hi:
        mid = (lo + (hi - 1)) // 2
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)
        merge2(arr, lo, mid, hi)


def partition(arr, lo, hi):
    pivot = lo
    boundary = lo
    for i in range(lo, hi):
        if arr[i] < arr[pivot]:
            boundary += 1
            arr[i], arr[boundary] = arr[boundary], arr[i]
    arr[pivot], arr[boundary] = arr[boundary], arr[pivot]
    return boundary


def quick_sort(arr, lo, hi):  # inclusive range assumed
    if lo < hi:
        pivot = partition(arr, lo, hi)
        quick_sort(arr, lo, pivot)
        quick_sort(arr, pivot + 1, hi)


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        k = i - 1
        while k >= 0 and arr[k] > key:
            arr[k + 1] = arr[k]
            k -= 1
        arr[k + 1] = key


def k_sort(arr, k):
    n = len(arr)
    for i in range(k, n, k):
        merge_sort(arr, i - k, min(i + k, n - 1))


def get_k_closest_point(arr, k, x):
    # up = upper_bound(arr, len(arr)-1, 0, x)
    n = len(arr)
    lo = lower_bound(arr, len(arr) - 1, 0, x)
    l = lo - 1 if arr[lo] == x else lo
    r = l + 1 if l == lo else l + 2
    print("l/r: ", l, r)
    i = 0
    closest = []
    while i < k:
        if l > 0:
            if r < n:
                if x - arr[l] < arr[r] - x:
                    closest.append(arr[l])
                    l -= 1
                else:
                    closest.append(arr[r])
                    r += 1
            else:
                closest.append(arr[l])
                l -= 1
        elif r < n:
            closest.append(arr[r])
            r += 1

        i += 1
    return closest


def swap(string, index_a, index_b):
    string[index_a], string[index_b] = string[index_b], string[index_a]


def permute(string, index):
    n = len(string)
    if index == n - 1:
        print(''.join(string))
        return

    for i in range(index, n):
        swap(string, i, index)
        permute(string, index + 1)
        swap(string, i, index)


def permute2(string, l, r):
    if l == r:
        print(''.join(string))
    else:
        for i in range(l, r + 1):
            swap(string, l, i)
            permute2(string, l + 1, r)
            swap(string, l, i)


def pathExist(puzzle, pos, n, m):
    x, y = pos
    if x < 0 or x > n or y < 0 or y > m:
        return False

    if puzzle[x][y] == 1:
        return True

    return False


def solve_maze(puzzle, solution, cur_pos, n, m):
    # Check if you can go right
    x, y = cur_pos
    solution[x][y] = 1
    if pathExist(puzzle, (x, y + 1), n, m):  # can go right
        solution[x][y + 1] = 1  # go right
        if solve_maze(puzzle, solution, (x, y + 1), n, m):
            return True
        else:
            solution[x][y + 1] = 0
    elif pathExist(puzzle, (x - 1, y), n, m):  # can go down
        solution[x - 1][y] = 1  # go down
        if solve_maze(puzzle, solution, (x - 1, y), n, m):
            return True
        else:
            solution[x - 1][y] = 0
    return False


def select_activity(activity_start, activity_end):  # [(10,20), (12,25), (20,30)]
    n = len(activity_end)
    selected = [0]
    for i in range(1, n):
        if activity_start[i] >= activity_end[selected[-1]]:
            selected.append(i)
    return selected


class Graph:

    def __init__(self, list_of_edges, vertices):
        self.INF = 100000
        self.edge_list = list_of_edges
        self.vertices = vertices
        self.graph = [[self.INF] * vertices for _ in range(vertices)]
        for edge in list_of_edges:
            x, y, weight = edge
            self.graph[x][y] = weight
            self.graph[y][x] = weight

    def mst(self):
        # sort list of edges
        mst_set = []
        edge_count = 0
        sorted(self.edge_list, key=lambda x: x[2])
        union_set = [i for i in range(self.vertices)]
        for edge in edge_list:
            if edge_count == self.vertices - 1:
                break
            v1, v2, weight = edge
            if union_set[v1] != union_set[v2]:
                union_set[v2] = union_set[v1]
                edge_count+=1
                mst_set.append(edge)


        return mst_set


if __name__ == '__main__':
    edge_list = [(0, 1, 4), (0, 3, 10), (0, 4, 2), (3, 4, 5), (3, 2, 5), (3, 1, 6), (1, 2, 3)]
    z = sorted(edge_list, key=lambda x: x[2])
    print(z)
