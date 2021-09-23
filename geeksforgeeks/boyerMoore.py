# https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
from typing import List

CHAR_SET_SIZE = 256


def getBadCharMap(pattern):
    badChar = [0] * CHAR_SET_SIZE

    for i, ch in enumerate(pattern):
        badChar[ord(ch)] = i  # stores last occurrence of each character in pattern

    return badChar


def findMatchIndices(string, pattern) -> List[int]:
    badCharMap = getBadCharMap(pattern)

    n, m = len(string), len(pattern)

    s = 0
    res = []
    recBreak=30
    while s <= n - m:
        j = m - 1

        while (n > s+j >= 0) and string[s+j] == pattern[j]:
            j -= 1

        if j < 0:
            res.append(s)

            s += (m - badCharMap[ord(string[s + m])]) if (s + m < n) else 1

        else:
            s += (j - badCharMap[ord(string[s + j])]) if (0 < s + j < n) else 1
        recBreak-=1
        if recBreak==0:
            break
    return res


if __name__=='__main__':
    string = 'ABCAABCD'
    pattern = 'ABC'

    print(findMatchIndices(string, pattern))