from copy import deepcopy

sol = []


def solveNqueen(n):
    x = [0] * n

    placeQueen(0, n, x)

    return sol


def place(k, i, x):  # can you place kth queen in ith column?
    for j in range(k):
        drow = abs(x[j] - (i + 1))  # row diff
        dcol = abs(j - k)  # column diff
        if x[j] == i + 1 or drow == dcol:  # this means any previous queen were placed in same column or diagonal
            return False
    return True


def placeQueen(k, n, x):  # place kth queen amongst n queen in n*n board
    global sol

    for i in range(n):

        if place(k, i, x):
            x[k] = i + 1
            if k == n - 1:
                sol.append(deepcopy(x))
            else:
                placeQueen(k + 1, n, x)


if __name__ == '__main__':
    result = solveNqueen(5)
    for i, res in enumerate(result):
        print(i + 1, res)
