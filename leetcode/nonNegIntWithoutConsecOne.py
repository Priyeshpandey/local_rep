# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3826/

class Solution:
    def get_bit_length(self,n):
        k = 0
        z = n
        while z:
            z = z >> 1
            k += 1
        return k

    def findIntegers(self, n: int) -> int:
        # check position of msb in n
        k = self.get_bit_length(n)

        fib = [0]*k
        fib[0], fib[1] = 1, 2

        for i in range(2,k):
            fib[i] = fib[i-1]+fib[i-2]

        lastBitOne = False
        res = 0
        bit = k-1

        while bit>=0:
            if (n & (1<<bit)) == 0:
                lastBitOne = False
            else:
                res+=fib[bit]
                if lastBitOne:
                    return res
                lastBitOne = True
            bit-=1

        return res+1







if __name__=='__main__':
    pass