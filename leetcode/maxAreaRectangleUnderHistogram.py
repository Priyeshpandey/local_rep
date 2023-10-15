# https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/
# todo : need to fix this, instead of returning min should return index of min in a range
from leetcode.custom_lib import binary_matrix_generator, printMatrix, generate_matrix_from_string
from math import log2
from sys import maxsize


def max_area_rect_under_hist_util(arr, start, end, segObj):
    if start == end:
        return arr[start]

    mid = segObj.rangeMinQuery(start, end)

    cur_area = (end - start + 1) * arr[mid]
    left_area = max_area_rect_under_hist_util(arr, start, mid - 1)
    right_area = max_area_rect_under_hist_util(arr, mid + 1, end)

    return max(cur_area, left_area, right_area)


class SegmentTree:
    def __init__(self, arr):
        self.segTree = []
        self.auxArr = arr
        self.bound_map = {}

    def minVal(self, x, y):
        if x==-1:
            return y
        if y==-1:
            return x

        return x if self.auxArr[x] < self.auxArr[y] else y

    def _constructSTutil(self, pos, start, end):
        if start > end:
            return maxsize
        if start == end:
            self.segTree[pos] = self.auxArr[start]
            self.bound_map[(start, end)] = pos
            return self.auxArr[start]

        mid = start + (end - start) // 2
        left = self._constructSTutil(2 * pos + 1, start, mid)
        right = self._constructSTutil(2 * pos + 2, mid + 1, end)
        self.segTree[pos] = min(left, right)
        self.bound_map[(start, end)] = pos
        return self.segTree[pos]

    def constructST(self):
        n = len(self.auxArr)
        size = 2 * int(2 ** log2(n)) - 1
        self.segTree = [0] * size
        self._constructSTutil(0, 0, n - 1)
        return self.segTree

    def _utilRangeMinQuery(self, start, end, lbound, rbound):
        if start > end:
            return -1
        if start == lbound and end == rbound:
            pos = self.bound_map[(start, end)]
            return self.segTree[pos]

        if start < lbound or end > rbound or start > rbound or end < lbound:
            return -1

        mid = lbound + (rbound - lbound) // 2
        left = self._utilRangeMinQuery(start, end if end < mid else mid, lbound, mid)
        right = self._utilRangeMinQuery(start if start > mid else mid + 1, end, mid + 1, rbound)
        return self.minVal(left, right)

    def rangeMinQuery(self, start, end):
        return self._utilRangeMinQuery(start, end, 0, len(self.auxArr) - 1)


# Approach 2, using stack

def max_area_rect(arr):
    n = len(arr)
    stack = []
    leftBound = [0]*n
    rightBound = [0]*n
    for i in range(n):
        if not stack or arr[stack[-1]] < arr[i]:
            leftBound[i] = i
            stack.append(i)
        else:
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            leftBound[i] = stack[-1]+1 if stack else 0
            stack.append(i)
    stack.clear()
    for i in range(n-1,-1,-1):
        if not stack or arr[stack[-1]] < arr[i]:
            rightBound[i] = i
            stack.append(i)
        else:
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            rightBound[i] = stack[-1]-1 if stack else n-1
            stack.append(i)

    print(leftBound, rightBound, sep='\n')

    maxArea = 0
    for i in range(n):
        area = arr[i]*(rightBound[i]-leftBound[i]+1)
        maxArea = max(maxArea,area)

    return maxArea



if __name__ == '__main__':
    arr = [2,1,5,6,2,3]
    print(max_area_rect(arr))
