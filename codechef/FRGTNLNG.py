T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    words = list(map(str, input().split()))
    phrase_list = []
    for _ in range(K):
        line = list(input().split())
        phrase_list.extend(line[1:])
    for word in words:
        if word in phrase_list:
            print('YES',end=' ')
        else:
            print('NO', end=' ')
    print('')