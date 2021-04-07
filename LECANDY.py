T = int(input())


def sum(S):
    val = 0
    for item in S:
        val += item
    return val


for i in range(T):
    N, C = map(int, input().split())
    candies = map(int, input().split())
    candy_sum = sum(candies)
    if candy_sum <= C:
        print('Yes')
    else:
        print('No')
