n, k = map(int, input().split())
N = 1000000007
queue = list(map(int, input().split()))

data = []


def get_junior_index(arr, index, junior, n, data):
    if index < n-1:
        if arr[junior] >= arr[index]:
            fear = data[n-junior-1][0]
            if fear == 1:
                return index
            else:
                junior_index = data[n-junior-1][1]
                if arr[junior_index] < arr[index]:
                    return junior_index
                else:
                    return get_junior_index(arr, index, junior_index, n, data)
        else:
            return junior

    else:
        return index


fearfullness = 1

for i in range(n - 1, -1, -1):
    if i == (n - 1):
        data.append((1, i))
        fearfullness *= 1
        fearfullness = fearfullness%N
    elif queue[i + 1] < queue[i]:
        data.append((2, i + 1))
        fearfullness*=2
        fearfullness = fearfullness%N
    else:
        junior_index = get_junior_index(queue, i, i+1, n, data)
        fear = junior_index - i + 1
        data.append((fear, junior_index))
        fearfullness*=fear
        fearfullness = fearfullness % N

print(fearfullness)