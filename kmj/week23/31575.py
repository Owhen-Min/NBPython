from collections import deque

def BFS(n, m, city_map):
    # 오른쪽, 아래쪽만 이동 가능
    dx = [1, 0]  # 오른쪽 이동
    dy = [0, 1]  # 아래쪽 이동

    queue = deque([(0, 0)])  # 시작 위치
    # 방문 여부 확인
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        # 목적지 도착 -> Yes 출력, 종료
        if x == n - 1 and y == m - 1:
            return "Yes"

        # 오른쪽, 아래 이동
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]

            # 범위 내 + 이동 가능 + 방문 X
            if 0 <= nx < n and 0 <= ny < m and city_map[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((nx, ny))

    # queue를 끝까지 돌았다 = 도착 x -> No
    return "No"

n, m = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(m)]

print(BFS(n, m, city_map))
