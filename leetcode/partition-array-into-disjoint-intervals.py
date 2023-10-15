# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = nums[0]
        min_ = nums[-1]
        max_arr = [0]*n
        min_arr = [0]*n

        for i in range(n):
            # build max_arr
            max_ = max(max_, nums[i])
            max_arr[i] = max_
            min_ = min(min_, nums[n-i-1])
            min_arr[n - i - 1] = min_
        # print(max_arr)
        # print(min_arr)
        k = 0
        for i in range(n-1):
            if max_arr[i] <= min_arr[i+1]:
                k = i+1
                break
        return k


if __name__=='__main__':
    sol = Solution()
    nums = [8,5,6,1,9,10,14,8]
    print(sol.partitionDisjoint(nums))