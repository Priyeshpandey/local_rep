from typing import List
import bisect


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            return arr[:k]
        if x > arr[-1]:
            n = len(arr)
            return arr[n - k:]
        lower_bound = bisect.bisect_left(arr, x, 0, len(arr) - 1)

        left_arr = []
        right_arr = []
        left = lower_bound - 1
        right = lower_bound
        j = 0
        while j < k:
            if left >= 0 and right < len(arr):
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left_arr.append(arr[left])
                    left -= 1
                else:
                    right_arr.append(arr[right])
                    right += 1
            elif left < 0 and right < len(arr):
                right_arr.append(arr[right])
                right += 1
            elif left >= 0 and right >= len(arr):
                left_arr.append(arr[left])
                left -= 1
            j += 1

        left_arr.reverse()
        return left_arr + right_arr


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k = 3
    x = 5
    print(sol.findClosestElements(arr, k, x))
