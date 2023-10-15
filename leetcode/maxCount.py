# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1
import bisect


class Solution:
    def rowWithMax1s(self, arr, n, m):
        max_row1 = -1
        index = m
        for i in range(n):
            cur_index = bisect.bisect_left(arr[i], 1, 0, m - 1)
            if arr[i][cur_index] == 0:
                continue
            if cur_index < index:
                index = cur_index
                max_row1 = i

        return max_row1


if __name__=='__main__':
    arr = [[0,0],[0,1],[0,0],[0,0],[0,1],[0,1]]
    sol = Solution()
    print(sol.rowWithMax1s(arr, len(arr), len(arr[0])))