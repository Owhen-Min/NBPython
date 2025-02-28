import sys

sys.setrecursionlimit(10000)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# 메모이제이션을 위한 DP 배열 초기화 (-1은 아직 계산되지 않았음을 의미)
dp = [[-1] * n for _ in range(m)]


def dfs(y, x):
    # 도착 지점에 도달하면 경로 하나를 찾았으므로 1 반환
    if y == m - 1 and x == n - 1:
        return 1

    # 이미 계산된 적이 있다면 그 값을 사용
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0  # 초기화 (경로의 수)

    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and board[y][x] > board[ny][nx]:
            dp[y][x] += dfs(ny, nx)

    return dp[y][x]


print(dfs(0, 0))