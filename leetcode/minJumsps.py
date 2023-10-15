#

from sys import maxsize
from random import randint


class Solution:
    def __init__(self):
        self.sol = {}

    def jumper(self, arr, index, n):
        if index == n:
            return 0
        if index in self.sol:
            return self.sol[index]
        max_steps = arr[index]
        if max_steps == 0:
            return maxsize
        if max_steps >= n - index:
            return 1
        jumps = maxsize
        for i in range(index + 1, min(index + max_steps, n - 1) + 1):
            jumps = min(jumps, 1 + self.jumper(arr, i, n))
        self.sol[index] = jumps
        return jumps

    def minJumps(self, arr, n):
        # code here
        if n == 1:
            return 0
        try:
            res = self.jumper(arr, 0, n - 1)
        except Exception as e:
            raise Exception(f'{arr}')
        if res == maxsize:
            return -1
        return res


# python program to count Minimum number
# of jumps to reach end

# Returns minimum number of jumps to reach arr[n-1] from arr[0]
def minJumps2(arr, n):
    # The number of jumps needed to reach the starting index is 0
    if n <= 1:
        return 0

    # Return -1 if not possible to jump
    if arr[0] == 0:
        return -1

    # initialization
    # stores all time the maximal reachable index in the array
    maxReach = arr[0]
    # stores the amount of steps we can still take
    step = arr[0]
    # stores the amount of jumps necessary to reach that maximal reachable position
    jump = 1

    # Start traversing array

    for i in range(1, n):
        # Check if we have reached the end of the array
        if i == n - 1:
            return jump

        # updating maxReach
        maxReach = max(maxReach, i + arr[i])

        # we use a step to get to the current index
        step -= 1

        # If no further steps left
        if step == 0:
            # we must have used a jump
            jump += 1

            # Check if the current index / position or lesser index
            # is the maximum reach point from the previous indexes
            if i >= maxReach:
                return -1

            # re-initialize the steps to the amount
            # of steps to reach maxReach from position i.
            step = maxReach - i
    return -1


if __name__ == '__main__':
    n = 20
    arr = [randint(1, 5) for _ in range(n)]
    print(arr)
    sol = Solution()
    jump1 = minJumps2(arr, n)
    jump2 = sol.minJumps(arr, n)
    assert jump1 == jump2, f'Mismatch {jump1} != {jump2}'
