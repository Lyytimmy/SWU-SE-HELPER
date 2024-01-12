"""
首先用一个表dp[i][j]来表示字符串1前面i个字符与字符串2前面j个字符最长的公共子序列
再想递归方程式：
当字符串1和字符串2的第i个和第j个字符串相同时：相当与dp[i-1][j-1]+1
当字符串1和字符串2的第i个和第j个字符不同时,我们有两个选择:
从字符串1中删除第i个字符,问题变为求dp[i-1][j],即前i-1个字符与字符串2的前j个字符的最长公共子序列。
从字符串2中删除第j个字符,问题变为求dp[i][j-1],即字符串1的前i个字符与字符串2的前j-1个字符的最长公共子序列。
"""
s1 = "abcdxyz"
s2 = "xyzabcd"
n = len(s1)
m = len(s2)

# 构建表
dp = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(m + 1):
    dp[i][0] = 0
for j in range(n + 1):
    dp[0][j] = 0

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

# 右下角最终结果
print(dp[m][n])