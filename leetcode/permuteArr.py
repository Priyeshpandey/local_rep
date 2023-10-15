# todo: complete this later
from typing import List
from itertools import permutations
from collections import deque
from random import randint

result = []
from copy import deepcopy


def permute(data, i, length):
    if i == length:
        print(''.join(data))
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]


class Solution:

    def __init__(self, nums: List[int]):
        self.default_array = nums
        self.array = nums
        self.resultList = []
        self._getPermutations(0)
        self.length = len(self.resultList)

    def _getPermutations(self, pos):
        if pos == len(self.array):
            self.resultList.append(deepcopy(self.array))
            return

        for i in range(pos, len(self.array)):
            self.array[i], self.array[pos] = self.array[pos], self.array[i]
            self._getPermutations(pos + 1)
            self.array[i], self.array[pos] = self.array[pos], self.array[i]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.default_array
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        index = randint(0, self.length - 1)
        # print(self.resultList)
        self.array = self.resultList[index]
        return self.array




def getAnyPermutation(arr):

    n = len(arr)
    if n==0:
        return
    if n==1:
        result.append(arr[0])
        return
    index = randint(0, n-1)
    result.append(arr[index])
    getAnyPermutation(arr[:index])
    getAnyPermutation(arr[index+1:])


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    getAnyPermutation(nums)
    print(result)
    # sol = Solution(nums)
    # print(sol.shuffle())
    # print(sol.shuffle())
    # print(sol.shuffle())
