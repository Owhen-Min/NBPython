n = int(input().strip())
stairs = [int(input().strip()) for _ in range(n)]

# n이 1,2 인 경우엔 모든 계단을 밟아야함
if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
# n >=3 부터는 dp 사용
else:
    # DP 배열
    dp = [0] * n
    dp[0], dp[1] = stairs[0], stairs[0] + stairs[1]  # 첫번째 계단 / 두번째까지 밟은 계단
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])  # 세번째까지 밟은 계단의 최댓값

    # dp 시작
    for i in range(3, n):
        # i-1를 밟고 올라오는 경우 -> stairs[i-2] 밟을 수 없음 -> i-3까지의 최대 점수 + stairs[i-1] + stairs[i]
        # i-2를 밟고 올라오는 경우 -> 지금까지 최대 점수 + stairs[i]
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[-1])
