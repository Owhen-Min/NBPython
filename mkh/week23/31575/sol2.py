from collections import deque

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
stack = deque()
stack.append((0,0))
deltas = ((1, 0), (0, 1))
ans = 'No'

while stack:
    curr_y, curr_x = stack.pop()
    if curr_y == m-1 and curr_x == n-1:
        ans = 'Yes'
        break
    for dy, dx in deltas:
        ny, nx = curr_y+dy, curr_x+dx
        if ny<m and nx<n and board[ny][nx]==1 and visited[ny][nx]==0:
            stack.append((ny, nx))
            visited[ny][nx]=1