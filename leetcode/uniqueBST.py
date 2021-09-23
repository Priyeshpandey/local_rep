from copy import deepcopy

result = []


def generatePermutation(k, A):
    global result
    if k == 1:
        result.append(deepcopy(A))
    else:
        generatePermutation(k - 1, A)

        for i in range(k - 1):
            if k % 2 == 0:
                A[i], A[k - 1] = A[k - 1], A[i]
            else:
                A[0], A[k - 1] = A[k - 1], A[0]

            generatePermutation(k - 1, A)


if __name__ == '__main__':
    n = 4
    generatePermutation(n, [i for i in range(1, n + 1)])

    for item in result:
        print(item)
