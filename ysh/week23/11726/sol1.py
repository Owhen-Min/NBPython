n = int(input())
dp = [i for i in range(n + 1)]
for j in range(3, n + 1):
    dp[j] = (dp[j - 1] + dp[j - 2]) % 10007
print(dp[n])