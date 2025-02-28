from collections import deque

deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))

M, N = map(int, input().split())
tomatos = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
total_tomatoes = 0

# Initialize the queue with all ripe tomatoes
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append((i, j, 0))  # (y, x, days)
        if tomatos[i][j] != -1:
            total_tomatoes += 1

max_days = 0
ripened = len(queue)

while queue:
    y, x, days = queue.popleft()

    for dy, dx in deltas:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and tomatos[ny][nx] == 0:
            tomatos[ny][nx] = 1
            ripened += 1
            queue.append((ny, nx, days + 1))

print(-1 if ripened < total_tomatoes else days)