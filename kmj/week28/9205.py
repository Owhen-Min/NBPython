from collections import deque

# BFS
def bfs(positions):
    n = len(positions)  # 전체 장소 수 (집 + 편의점 + 페스티벌)
    visited = [False] * n  # 방문 여부
    
    # bfs 사전작업
    queue = deque()
    queue.append(0)  # 집(시작)
    visited[0] = True  # 집 방문 표시

    while queue:
        cur=queue.popleft() # 현재 위치

        # 도착
        if cur == n - 1:
            return "happy"

        # 아직 방문하지 않았고, 거리가 1000m 이하인 곳만 이동 가능
        for i in range(n):
            if not visited[i]:
                dist = abs(positions[cur][0] - positions[i][0]) + abs(positions[cur][1] - positions[i][1]) # 거리 계산
                if dist <= 1000:
                    visited[i] = True
                    queue.append(i)

    # 도착 못함 -> 실패
    return "sad"
    
t = int(input()) # 테케 수
for _ in range(t):
    store = int(input()) # 편의점 갯수
    # 집, 편의점, 페스티벌 좌표
    positions = [tuple(map(int, input().split())) for _ in range(store + 2)]
    print(bfs(positions))
