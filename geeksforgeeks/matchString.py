# https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/
from typing import List


def i_search(ii, i, j, n, m, string, matrix):
    found = 0

    if 0<=i<=n and 0<=j<=m and string[ii]==matrix[i][j]:
        match = string[ii]
        ii+=1
        matrix[i][j] = 0

        if ii == len(string):
            found = 1

        else:
            found += i_search(ii, i, j - 1, n, m, string, matrix) \
                     + i_search(ii, i, j + 1, n, m, string, matrix) \
                     + i_search(ii, i - 1, j, n, m, string, matrix) \
                     + i_search(ii, i + 1, j, n, m, string, matrix)
        matrix[i][j] = match

    return found


def matchStr(string, matrix, n, m):
    count = 0

    for i in range(n):
        for j in range(m):
            count += i_search(0, i, j, n - 1, m - 1, string, matrix)

    return count


if __name__=='__main__':
    matrix = [
        ['a','b','c','d'],
        ['a','p','c','d'],
        ['p','r','x','d'],
        ['a','o','r','x'],
        ['a','a','p','d']

    ]
    string = 'pro'
    n, m = len(matrix), len(matrix[0])
    print(matchStr(string, matrix, n, m))