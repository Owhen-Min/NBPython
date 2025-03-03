def dfs(node):
    visited[node] = True  # 방문 처리
    count = 1  # 자기 자신도 감염되므로 1부터 시작
    for neighbor in graph[node]:  # 연결된 모든 컴퓨터 탐색
        if not visited[neighbor]:  # 방문하지 않은 경우
            count += dfs(neighbor)  # 재귀
    return count

C = int(input())  # 컴퓨터 수
N = int(input())  # 네트워크 연결 수
graph = [[] for _ in range(C+1)]
visited = [False] * (C+1)  # 방문 리스트

# 인접리스트
for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS (1번 컴퓨터에서 시작)
infected_cnt = dfs(1) - 1  # 1번 컴퓨터 제외한 감염된 수 (1번 컴퓨터를 통해 감염된 컴퓨터 수 구하기)

print(infected_cnt)


"""
# 인접리스트 결과
[
    [],       # 0 (x)
    [2, 5],   # 1번 com
    [1, 3, 5],# 2번 com
    [2],      # 3번 com
    [7],      # 4번 com
    [1, 2, 6],# 5번 com
    [5],      # 6번 com
    [4]
]
# [2, 5] # 2번 방문 '+1'
## 2번 부터 방문 시작
# 2 -> [1,3,5] # 3,5번 방문(1 이미 o) '+3'
# 3 -> [2] (2 이미 ㅇ)
# 5 -> [1,2,6] # 6번 방문 (1,2 이미 ㅇ) '+4'
# 6 -> [5] (5 이미 ㅇ)

## 5번 방문 (이미 ㅇ)
"""
