from sys import maxsize


def minCost(word, k, index):
    if index == len(word) or index == len(word) - 1:
        return 0

    n = len(word)
    min_cost = maxsize
    fill = 0
    for i in range(index, n):
        # calculate how much line is filled
        fill += word[i]
        # calculate cost if line is not exhausted
        # calculate extra spaces
        extra_space = i - index
        if fill + extra_space <= k:
            cost = ((k - fill - extra_space) ** 2) if i < n - 1 else 0
            if cost < min_cost:
                min_cost = min(min_cost, cost + minCost(word, k, i + 1))
        else:
            break
    print(index, ":", min_cost)
    return min_cost


def minCostDP(word, k):
    n = len(word)
    space = [[0] * (n + 1) for _ in range(n + 1)]
    inf = maxsize

    for i in range(1, n + 1):
        space[i][i] = k - word[i - 1]
        for j in range(i+1, n + 1):
            space[i][j] = space[i][j - 1] - word[j - 1] - 1

    lc = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i, n + 1):
            if space[i][j] < 0:
                lc[i][j] = inf
            elif j == n and space[i][j] >= 0:
                lc[i][j] = 0
            else:
                lc[i][j] = space[i][j] ** 2

    cost = [0] * (n + 1)
    cost[0] = 0
    for j in range(1, n + 1):
        cost[j] = inf
        for i in range(1, j + 1):
            if (cost[i - 1] != inf and
                    lc[i][j] != inf and
                    ((cost[i - 1] + lc[i][j]) < cost[j])):
                cost[j] = cost[i - 1] + lc[i][j]

    return cost[n]


if __name__ == '__main__':
    word = [3, 2, 2, 4, 4]
    # word = [4, 4]
    k = 5
    # print(len(word))
    # print(*word)
    print(minCostDP(word, k))
