# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3807/

class SolutionX:
    def findLength(self, nums1, nums2) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        dp = [[0]*(n2+1) for _ in range(n1+1)]
        result = 0
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j] = 0
                elif nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                result = max(result,dp[i][j])
        for row in dp:
            print(*row)
        return result





class SolutionBruteForce:

    def findLength(self, nums1, nums2) -> int:
        if nums1 == nums2:
            return len(nums1)

        n1 = len(nums1)
        n2 = len(nums2)

        if n1 < n2:
            while n1 >= 0:
                for i in range(0, len(nums1) - n1 + 1):
                    for j in range(0, len(nums1) - n1 + 1):
                        if nums1[i:n1 + i + 1] == nums2[j:n1 + j + 1]:
                            return len(nums1[i:n1 + i + 1])

                n1 -= 1
        else:
            while n2:
                for i in range(0, len(nums2) - n2 + 1):
                    for j in range(0, len(nums2) - n2 + 1):
                        if nums1[i:n2 + i + 1] == nums2[j:n2 + j + 1]:
                            return len(nums1[i:n2 + i + 1])

                n2 -= 1
        for x in nums1:
            if x in nums2:
                return 1

        return 0





if __name__ == '__main__':
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 1, 4, 7]
    sol = SolutionX()
    print(sol.findLength(a, b))
