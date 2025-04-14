import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)
deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))


def dfs(y, x):
    board[y][x] = 0
    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx]:
            dfs(ny, nx)


t = int(input())
for tc in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    ans = 0

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                dfs(i, j)
                ans += 1

    print(ans)
