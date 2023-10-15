t = int(input())


def get_even_index(array, start):
    n = len(array)
    for i in range(start, n):
        if array[i] % 2 == 0:
            return i
    return -1


def get_odd_index(array, start):
    n = len(array)
    for i in range(start, n):
        if array[i] % 2 == 1:
            return i
    return -1


def rearrange(array):
    n = len(array)
    for i in range(n - 1):
        if array[i] % 2 == 0:
            index = get_even_index(array, i + 1)
            if index != -1:
                array[i + 1], array[index] = array[index], array[i + 1]
        if array[i] % 2 == 1:
            index = get_odd_index(array, i + 1)
            if index != -1:
                array[i + 1], array[index] = array[index], array[i + 1]
    return array


for _ in range(t):
    n = int(input())
    heights = list(map(int, input().split()))
    heights = rearrange(heights)
    for height in heights:
        print(height, end=' ')
    print('')

