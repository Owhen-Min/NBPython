from collections import deque

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())  # 가로, 세로, 배추 수
    cabbage_positions = [tuple(map(int, input().split())) for _ in range(K)]

    # 밭 생성 (0: 배추 없음, 1: 배추 있음)
    field = [[0] * M for _ in range(N)]

    # 배추 심기
    for x, y in cabbage_positions:
        field[y][x] = 1

    # 방문 여부
    visited = [[False] * M for _ in range(N)]

    def bfs(start_x, start_y):
        queue = deque()
        queue.append((start_x, start_y))
        visited[start_y][start_x] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < M and 0 <= ny < N:
                    if field[ny][nx] == 1 and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

    # 지렁이 수 세기
    worm_count = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                bfs(x, y)
                worm_count += 1

    print(worm_count)
