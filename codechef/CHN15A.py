T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    minions = list(map(int, input().split()))
    count = 0
    for minion in minions:
        if (minion + K) % 7 == 0:
            count += 1
    print(count)