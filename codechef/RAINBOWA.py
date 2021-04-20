
#

def basic_check(array):
    N = len(array)
    if array[0] != 1 or array[N-1] !=1:
        return False
    if N%2==0:
        if array[N//2] != 7 or array[N//2 -1] != 7:
            return False
    else:
        if array[N//2] !=7:
            return False
    return True


def is_rainbow(array,N):
    rainbow = [0 for _ in range(8)]
    rainbow[1]=1
    rainbow[7]=1
    i=1
    j=N-2
    while(i<=j):
        if array[i] > 7:
            return False
        if array[i]!=array[j]:
            return False
        if not ((array[i-1] == array[i]) or (array[i-1] == array[i]-1)):
            return False
        rainbow[array[i]] = 1
        i += 1
        j -= 1

    for k in range(1,8):
        if rainbow[k] == 0:
            return False
    return True




T = int(input())

for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))

    if basic_check(array):
        if is_rainbow(array,N):
            print('yes')
        else:
            print('no')
    else:
        print('no')