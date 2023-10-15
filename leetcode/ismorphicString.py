# https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3811/

def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    asciiMap = ['' for _ in range(256)]

    n = len(s)

    for i in range(n):
        target = asciiMap[ord(s[i])]
        if target:
            if t[i] == target:
                continue
            else:
                return False
        if t[i] in asciiMap:
            return False
        asciiMap[ord(s[i])] = t[i]

    return True


if __name__ == "__main__":
    s = "bbbaaaba"
    t = "aaabbbab"
    print(isIsomorphic(s, t))
