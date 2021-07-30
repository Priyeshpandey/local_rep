def strCompare(str1,str2,start):
    n = len(str1)

    for i in range(start,n+start):
        if str1[i-start] == str2[i%n]:
            continue
        else:
            return False
    return True


def isEqual(str1, str2):
    if str1 == str2:
        return True

    n = len(str1)

    for start in range(n):
        if strCompare(str1, str2, start):
            return True

    return False


if __name__=='__main__':
    str1 = "fkjsdfhalshfakafsdkjh"
    str2 = "dkjhfkjsdfhalshfakafs"

    print(isEqual(str1,str2))