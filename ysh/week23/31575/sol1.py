n, m = map(int, input().split())  # 가로 n, 세로 m
map_info = [list(map(int, input().split())) for _ in range(m)]

stack = [(0, 0)]
delta = [(0, 1), (1, 0)]
visited = [[0] * n for _ in range(m)]
answer = "No"

while stack:
    y, x = stack.pop()
    if visited[y][x]:
        continue
    visited[y][x] = True

    if y == m - 1 and x == n - 1:
        answer = "Yes"
        break

    for dy, dx in delta:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and map_info[ny][nx] and not visited[ny][nx]:
            stack.append((ny, nx))

print(answer)