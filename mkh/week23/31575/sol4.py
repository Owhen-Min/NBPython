n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]

visited[0][0] = 1

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            if i > 0:
                visited[i][j] |= visited[i-1][j]
            if j > 0:
                visited[i][j] |= visited[i][j-1]

print("Yes" if visited[m-1][n-1] else "No")
