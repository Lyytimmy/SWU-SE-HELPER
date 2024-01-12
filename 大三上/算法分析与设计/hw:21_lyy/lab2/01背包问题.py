weights = [1, 3, 4]
values = [15, 20, 30]
capacity = 4
n = len(weights)
dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, capacity+1):
        if j < weights[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(
                dp[i-1][j],
                dp[i-1][j-weights[i-1]] + values[i-1]
            )
print(dp[n][capacity])