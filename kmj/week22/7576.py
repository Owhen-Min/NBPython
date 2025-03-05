from collections import deque

# 상황 1 : 모든 토마토가 이미 익어있으면 0 출력
# 상황 2 : BFS가 끝난 후, 익지 않은 토마토(0)가 남아있으면 -1 출력
# 상황 3 : 모든 토마토가 익었다면 최소 일수 출력

def bfs():
    queue = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:  # 익은 토마토(1)를 모두 넣음
                queue.append((i, j))
    
    min_day = -1  # 최소 일수 (BFS 실행 횟수)
    
    while queue:
        min_day += 1  # 하루 증가
        for _ in range(len(queue)):  # 현재 큐에 있는 모든 요소 처리
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 상하좌우
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    graph[nx][ny] = 1  # 익음 처리
                    queue.append((nx, ny))
    
    # 상황2 : BFS가 끝난 후, 익지 않은 토마토(0)가 남아있으면 -1 출력
    for row in graph:
        if 0 in row:
            print(-1)
            return

    # 상황 3 : 모든 토마토가 익었다면 최소 일수 출력
    print(min_day)

# 모든 토마토가 이미 익어있는지 확인하는 함수 (상황 1 )
def all_ripe(graph):
    for row in graph:
        for cell in row:
            if cell == 0:  # 안 익은 토마토가 하나라도 있으면 False
                return False
    return True  # 전부 1 또는 -1이면 True

## 시작
M, N = map(int, input().split())  # 가로: M / 세로:  N
graph = [list(map(int, input().split())) for _ in range(N)]

# 상황1 : 모든 토마토가 이미 익어있으면 0 출력
if all_ripe(graph):
    print(0)
# 아니면 bfs 시작
else:
    bfs()
