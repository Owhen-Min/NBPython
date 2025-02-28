import sys
from functools import lru_cache

sys.setrecursionlimit(50000)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
deltas = [(-1, 0), (1, 0), (0, 1), (0, -1)]


@lru_cache(None)
def dfs(y, x):
    # 도착 지점에 도달하면 경로 하나를 찾았으므로 1 반환
    if y == m - 1 and x == n - 1:
        return 1

    total_paths = 0

    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and board[y][x] > board[ny][nx]:
            total_paths += dfs(ny, nx)

    return total_paths


print(dfs(0, 0))