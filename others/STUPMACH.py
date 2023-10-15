t = int(input())


def count_tokens(array, start, end):
    if start == end:
        return array[start]
    min_index = 0
    for i in range(start, end):
        if array[i] < array[min_index]:
            min_index = i
    min_val = array[min_index]
    for i in range(start, end):
        array[i] -= min_val
    return min_val * end + count_tokens(array, start, min_index)


for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(count_tokens(array, 0, n))
