n = int(input())
ls = [int(input()) for _ in range(n)]
dp = [0]*(max(ls)+1)

# 최고로 큰 숫자가 3 미만일 경우 dp 배열에서 index error가 나올 수 있으므로 try except로 처리한다.
try:
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
except:
    pass

# 모든 값들을 한번에 계산해서 불필요한 추가 계산이 없도록 만든다. 해당 문제는 작은 문제들의 합의 형태다.
# 메모이제이션으로 볼 수도 있다.
for i in range(4, max(ls)+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for num in ls:
    print(dp[num])