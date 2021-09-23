# https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1#
class SolutionBruteForce:
    def lps(self, s):
        # code here
        n = len(s)
        mid = n // 2
        prefix, suffix = 0, mid
        length = n - 1
        max_len = 0
        while length:
            cur_len = length
            prefix, suffix = 0, n - length
            while suffix < n and s[prefix] == s[suffix]:
                prefix += 1
                suffix += 1
        if suffix == n and length > max_len:
            max_len = length
            length -= 1

        return max_len
