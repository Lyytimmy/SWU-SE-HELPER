n = 4
t = [3, 2, 1, 4]
m = 2  # 流水线数量

# 初始化dp table
dp = [[-1 for _ in range(n)] for _ in range(n)]

# 填写base case
for i in range(n):
    dp[i][i] = t[i]

# 使用动态规划填写dp table
for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp[i][j] = min(dp[i][k] + dp[k + 1][j] + max(t[i], t[j]) for k in range(i, j))

print(dp[0][n - 1])  # 输出最短调度时间