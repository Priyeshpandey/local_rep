def permute(string, i):
    if i == len(string):
        print(''.join(string))
        return

    for x in range(i, len(string)):
        string[i], string[x] = string[x], string[i]
        permute(string, i + 1)
        string[i], string[x] = string[x], string[i]


def splitString(string):
    n = len(string)
    counter = [0, 0]
    splitCount = 0

    for i in range(n):
        counter[int(string[i])] += 1
        if counter[0] == counter[1] and counter[0] != 0:
            splitCount += 1
            counter = [0, 0]

    if counter[0]!=counter[1]:
        return -1

    return splitCount


if __name__ == '__main__':
    string = "10101010"
    print(splitString(string))