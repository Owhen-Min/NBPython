from collections import deque

tc = 0
deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
while True:
    tc += 1
    n = int(input())
    if n == 0:
        break
    board = [list(map(int,input().split())) for _ in range(n)]
    visited = [[2500]*n for _ in range(n)]
    visited[0][0] = board[0][0]
    q = deque([(0,0)])
    while q:
        y, x = q.popleft()
        for dy, dx in deltas:
            ny, nx = y+dy, x+dx
            if 0<=ny<n and 0<=nx<n and visited[ny][nx] > visited[y][x]+board[ny][nx]:
                visited[ny][nx] = visited[y][x]+board[ny][nx]
                q.append((ny, nx))

    print(f'Problem {tc}: {visited[n-1][n-1]}')