def findCatalan(n):
    if n < 2:
        return 1
    # return the nth Catalan number.
    C = [0] * (n + 2)
    C[0] = 1
    C[1] = 1
    for x in range(2, n + 2):
        C[x] = 0
        for i in range(x):
            C[x] += C[i] * C[x - i]

    return C[n + 1]


if __name__ == '__main__':
    for i in range(10):
        print(i,':', findCatalan(i), end=', ')