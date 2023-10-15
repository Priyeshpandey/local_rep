# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3809/
import random

N = 10 ** 9 + 7


class Solution:
    def __init__(self):
        self.map = {
            '10': 1,
            '20': 1,
            '*0': 2
        }

    def isAtom(self, item):
        if len(item) > 2:
            return False

        if item in ['0', '00'] or item[0] == '0':
            return False
        if '*' in item or int(item) > 26:
            return False
        return True

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            print('Failed')
            return 0
        atom_list = []
        i = 0
        pool = [f'{i}' for i in range(1, 10)] + ['*']
        while i < len(s):
            if s[i] in pool:
                atom_list.append(s[i])

            else:
                x = atom_list[-1][-1]
                if x == '*':
                    atom_list[-1] += s[i]

                elif x == '0' or int(x) > 2:
                    print('Failed')
                    return 0
                else:
                    atom_list[-1] += s[i]
            i += 1

        print(atom_list)

        return self.getResult(atom_list)

    def getResult(self, atom_list):
        if len(atom_list) == 0:
            return 1

        if len(atom_list) == 1:
            if len(atom_list[0]) > 1:
                if not self.isAtom(atom_list[0]):
                    return 0
                return self.map[atom_list[0]]

            if atom_list[0] == '*':
                return 9
            return 1

        if len(atom_list) == 2:

            a, b = atom_list
            if not self.isAtom(a + b):
                return 1
            if '*' not in atom_list:
                if b == '0':
                    return 1
                if int(a + b) < 27:
                    return 2
                return 1
            if a + b == '**':
                return 96

            if a + b == '*0':
                return 2

            if a == '*':
                if int(b) < 7:
                    return 9
                return 3
            if b == '*':
                if int(a) == 1:
                    return 18
                if int(a) == 2:
                    return 15
                return 9

        result = (self.getResult(atom_list[:1]) * self.getResult(atom_list[1:]) +
                  self.getResult(atom_list[:2]) * self.getResult(atom_list[2:])) % N
        return result


class SolutionX:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = dp[0] * self.decodeOne(s[0])

        for i in range(2, n + 1):
            prev_char = s[i - 2]
            curr_char = s[i - 1]
            dp[i] += dp[i - 1] * self.decodeOne(curr_char) + dp[i - 2] * self.decodeTwo(prev_char, curr_char)

        print(dp)
        return dp[n]%N

    def decodeOne(self, char):
        if char == '*':
            return 9
        if char == '0':
            return 0
        return 1

    def decodeTwo(self, prev, curr):
        if prev == '0':
            return 0
        if (prev + curr) == '**':
            return 15 #96

        if prev == '*':
            if curr == '0':
                return 2
            if int(curr) < 7:
                return 2 #11
            return 1 #10

        if curr == '*':
            if prev == '1':
                return 9 #18
            if prev == '2':
                return 6 #15
            return 0

        if int(prev) < 3:
            if curr == '0':
                return 1
            if int(prev + curr) < 27:
                return 1
            return 0

        if curr == '0':
            return 0

        return 0


if __name__ == '__main__':
    pool = [f'{i}' for i in range(10)] + ['*']
    n = 29
    test_str = ''.join([pool[random.randint(0, len(pool) - 1)] for _ in range(n)])
    # test_str = "697*"
    print(test_str)
    sol = SolutionX()
    result = sol.numDecodings(test_str)
    print('Result: ', result)
