def knapsack(deliveries, capacity):

    n = len(deliveries)

    dp = [[0] * (capacity + 1)
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        weight = deliveries[i - 1].weight
        profit = deliveries[i - 1].profit

        for w in range(capacity + 1):

            if weight <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    profit + dp[i - 1][w - weight]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    selected = []
    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:
            selected.append(deliveries[i - 1])
            w -= deliveries[i - 1].weight

    selected.reverse()

    return selected, dp[n][capacity]