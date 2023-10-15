T = int(input())


def isLP(lookup, string):
    N = len(string)
    l_string = string[:N // 2]
    r_string = string[N // 2 if N % 2 == 0 else N // 2 + 1:]
    for i in range(len(l_string)):
        if l_string[i] in lookup:
            lookup[l_string[i]] += 1
        else:
            lookup[l_string[i]] = 1

    for j in range(len(r_string)):
        if r_string[j] not in lookup:
            return 'NO'
        else:
            lookup[r_string[j]] -= 1

    for key in lookup.keys():
        if lookup[key] != 0:
            return 'NO'

    return 'YES'


for _ in range(T):
    string = input()
    lookup = {}
    print(isLP(lookup, string))
