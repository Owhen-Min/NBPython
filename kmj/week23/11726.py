# 피보나치 수열이구나~~, 40초가 걸리는구나..
# dp[i] = (dp[i-1] + dp[i-2])

n = int(input())

dp = [0] * (n+1)  # dp 배열
dp[1] = 1  # n=1일 때

if n >= 2:
    dp[2] = 2  # n=2일 때

# n=2 일 땐 실행 X, n>=2부턴 dp[2] 값이 필요하므로 하나의 분기에 넣음
for i in range(3, n+1):  # n>=3 때 만 for문 실행
    dp[i] = (dp[i-1] + dp[i-2]) % 10007  # 점화식(피보나치)

print(dp[n])
