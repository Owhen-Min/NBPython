board = [list(map(int,input().split())) for _ in range(5)]
r, c = map(int,input().split())
deltas = ((1,0), (-1,0), (0,1), (0,-1))
def dfs(depth, y, x, visited, value):
    if depth == 3:
        return value

    total = 0

    for dy, dx in deltas:
        ny, nx = y+dy, x+dx
        if 0<=ny<5 and 0<=nx<5 and (ny, nx) not in visited and board[ny][nx] != -1:
            visited.add((ny,nx))
            if board[ny][nx] == 1:
                total = max(dfs(depth+1, ny, nx, visited, value+1), total)
            else:
                total = max(dfs(depth + 1, ny, nx, visited, value), total)
            visited.remove((ny,nx))

    return total

if dfs(0, r, c, {(r,c)}, 0) >=2:
    print(1)
else:
    print(0)