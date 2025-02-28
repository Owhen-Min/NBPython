n = list(map(int,input()))
l = len(n)
dp = [0 for _ in range(l+2)]
if (n[0] == 0) :
    print("0")
else :
    dp[0], dp[1] = 1, 1
    for i in range(1, l):
        if n[i] > 0:
            dp[i+1] += dp[i]
        temp = n[i-1] * 10 + n[i]
        if temp >= 10 and temp <= 26 :
            dp[i+1] += dp[i-1]
    print(dp[l] % 1000000)