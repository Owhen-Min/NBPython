n = int(input())
tps = [list(map(int,input().split())) for _ in range(n)]
dp = [0] * (n + 1)

for i in range(n):
    time, value = tps[i]
    if i + time <= n:
        dp[i+time] = max(max(dp[:i+1])+value, dp[i+time])

print(max(dp))