from collections import deque

m, n = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
deltas = ((-1,0), (1,0), (0, 1), (0,-1))
ans = 0

q = deque([[0,0]])

while q:
     y, x = q.pop()
     if y == m-1 and x == n-1:
         ans += 1
         continue
     for dy, dx in deltas:
         ny, nx = y+dy, x+dx
         if 0<= ny < m and 0<= nx < n and board[y][x] > board[ny][nx]:
             q.append((ny, nx))

print(ans)
