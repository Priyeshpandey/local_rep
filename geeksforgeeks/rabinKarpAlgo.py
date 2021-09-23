def get_hash(meta, target=None, prevHash=None, prevChar=None,
             nextChar=None, roll=False) -> int:
    """
    Base : 26
    a -> 1
    z -> 26
    base = meta[base]
    length = meta[size]

    :param target:
    :param prevHash:
    :param nextChar:
    :param roll:
    :return:
    """
    base = meta['base']
    k = meta['size']

    if roll:
        toRemove = (ord(prevChar) - ord('a') + 1) * (base ** (k - 1))
        toAdd = (ord(nextChar) - ord('a') + 1)
        new_hash = (prevHash - toRemove)*base + toAdd

        return new_hash
    # else calculate startHash
    sum_ = 0
    i = 0
    while k:
        k -= 1
        sum_ += (ord(target[i]) - ord('a') + 1) * (base ** k)
        i += 1

    return sum_


def patternMatch(src: str, target: str) -> list[int]:
    n = len(target)
    m = len(src)
    meta = {
        'base': 26,
        'size': n
    }
    result = []
    target_hash = get_hash(meta,target)
    print(target_hash)
    prev_hash = get_hash(meta, src[:n])
    print(prev_hash)
    if prev_hash == target_hash:
        if src[:n] == target:
            result.append(0)

    for i in range(n, m):
        next_hash = get_hash(meta, prevChar=src[i-1], prevHash=prev_hash, nextChar=src[i], roll=True)
        print(src[i:i+n], next_hash)
        if next_hash == target_hash:
            print('Match')
            if src[i:i + n] == target:
                result.append(i)
        prev_hash = next_hash

    return result


if __name__=='__main__':
    src = "babbabababbabaabbbaaa"
    target="bab"
    print(patternMatch(src, target))