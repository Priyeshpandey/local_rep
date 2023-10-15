# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3816/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                L = j + 1
                R = n - 1
                aux_target = target - (nums[i] + nums[j])
                while L < R:
                    if nums[L] + nums[R] == aux_target:
                        res = [nums[i], nums[j], nums[L], nums[R]]
                        res.sort()
                        if res not in result:
                            result.append(res)
                        L += 1
                        R -= 1
                    elif nums[L] + nums[R] < aux_target:
                        L += 1
                    else:
                        R -= 1

        return result


if __name__=='__main__':
    nums = [1,0,-1,0,-2,2]
    target = 0
    sol = Solution()
    print(sol.fourSum(nums,target))