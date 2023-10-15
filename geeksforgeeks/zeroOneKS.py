def knapSack(index, Capacity, weight, values):
    if index < 0 or Capacity <= 0:
        return 0
    include = 0
    if weight[index] <= Capacity:
        include = values[index] + knapSack(index - 1, Capacity - weight[index], weight, values)
    exclude = knapSack(index - 1, Capacity, weight, values)

    return max(include, exclude)


def knapSackTable(Capacity, weight, values):
    n = len(weight)

    dp = [[0]*(Capacity+1) for _ in range(n+1)]

    for item in range(1,n+1):
        for wt in range(Capacity+1):
            if wt - weight[item-1] >= 0:
                dp[item][wt] = max(dp[item-1][wt], values[item-1] + dp[item][wt - weight[item-1]])
            else:
                dp[item][wt] = dp[item-1][wt]

    return dp[n][Capacity]


if __name__ == '__main__':
    W = 100
    values = [11, 20, 31, 10]
    weight = [40, 50, 60, 22]
    n = len(values)

    print(knapSack(n - 1, W, weight, values))
    print(knapSackTable(W,weight,values))
