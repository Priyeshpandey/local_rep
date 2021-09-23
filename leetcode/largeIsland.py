# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3835/
from collections import deque
from copy import deepcopy
from leetcode.custom_lib import binary_matrix_generator, printMatrix


def findSize(space, x, y, n, m):
    if (x < 0 or x >= n) or (y < 0 or y >= m) or (space[x][y] != 1):
        return 0
    space[x][y] = 2
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    area = 0
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        area += findSize(space, nx, ny, n, m)

    # print((x,y),":",area)
    return 1 + area


def annotateSpace(space, markerMap, marker, x, y, n, m):
    if (x < 0 or x >= n) or (y < 0 or y >= m) or space[x][y] != 1:
        return 0

    space[x][y] = marker
    markerMap[marker] += 1

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        annotateSpace(space, markerMap, marker, nx, ny, n, m)

    return 0


def maxIsland(space):
    n = len(space)
    m = len(space[0])

    q = deque()
    marker = 2
    markerMap = {}
    for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                q.append((i, j))
            else:
                markerMap[marker] = 0
                annotateSpace(space, markerMap, marker, i, j, n, m)
                marker += 1

    max_area = 0
    print(markerMap)
    if not q:
        return n * m
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while q:
        x, y = q.popleft()
        area = set()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n) and (0 <= ny < m) and space[nx][ny] != 0:
                area.add(space[nx][ny])
        area_sum = 1
        for key in area:
            area_sum += markerMap[key]

        max_area = max(area_sum, max_area)

    return max_area


if __name__ == '__main__':
    space = binary_matrix_generator(4, 4)
    printMatrix(space)
    # print(space)
    print(maxIsland(space))
