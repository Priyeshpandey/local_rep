# https://leetcode.com/problems/count-and-say/

def countAndSay(n: int) -> str:
    if n == 1:
        return "1"

    if n == 2:
        return "11"

    res = countAndSay(n - 1)
    n = len(res)
    i = 0

    count = 0
    sol = ''
    while i < n - 1:
        if res[i] == res[i + 1]:
            count += 1
        else:
            sol += str(count + 1) + res[i]
            count = 0
        i += 1

    if res[i] != res[i - 1]:
        sol += "1" + res[i]
    else:
        sol += str(count + 1) + res[i]
    return sol