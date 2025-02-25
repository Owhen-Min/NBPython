def max_sum(n, stairs):

    if n == 1:
        return stairs[0]
    elif n == 2:
        return stairs[0] + stairs[1]

    dp = [0] * n
    dp[0] = stairs[0]  # 첫 번째 계단
    dp[1] = stairs[0] + stairs[1]  # 첫 번째 + 두 번째 계단
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])  # 한 번에 두 칸 or 한 칸 한 칸

    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    return dp[-1]  # 마지막 계단 점수 반환

N = int(input())

stairs = [int(input()) for _ in range(N)]
# print(stairs)
print(max_sum(N, stairs))