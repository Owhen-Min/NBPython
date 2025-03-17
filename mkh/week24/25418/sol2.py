n, k = map(int,input().split())
dp = [1e9]*(k+1)
dp[n] = 0
for i in range(n+1, k+1):
    if i % 2:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = min(dp[i-1], dp[i//2])+1

print(dp[k])