def common(w1, w2):
    iw2 = 0

    for iw1 in range(len(w1)):
        while iw2 < len(w2) and w1[iw1] != w2[iw2]:
            iw2 += 1

        if iw2 == len(w2):
            return False
        iw2 += 1

    return True


def findLUSlength(strs):
    N = len(strs)
    strs.sort(key=lambda x: len(x), reverse=True)

    for i, word in enumerate(strs):
        found = False
        for j in range(N):

            if i!=j and len(strs[j]) >= len(word) and common(strs[i], strs[j]):
                found = True
                break

        if not found:
            return len(word)

    return -1



if __name__ == '__main__':
    w1 = 'abc'
    w2 = 'absdc'
    strs = ["aaa","aaa","aa"]
    # assert (w1 == w2) == common(w1,w2), 'not same!'
    print('common' if common(w1, w2) else 'not common')
    print(findLUSlength(strs))