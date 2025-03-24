from collections import deque

# DFS
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ') # 한 줄 출력
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(graph, next_v, visited)

# BFS
def bfs(graph, start):
    visited = [False] * (len(graph))
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ') # 한 줄 출력
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                queue.append(next_v)

# 정점, 간선, 시작 정점 번호
n, m, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 인접 리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#print(graph) # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]


# 번호가 작은 정점부터 방문하도록 정렬
for adj in graph:
    adj.sort()

# DFS
visited_dfs = [False] * (n + 1)
dfs(graph, s, visited_dfs)
print() # 줄바꿈 (DFS 출력 후, 줄 바꿔서 BFS 출력)

# BFS
bfs(graph, s)
