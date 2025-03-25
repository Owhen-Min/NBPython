from collections import defaultdict, deque

n, m, v = map(int, input().split())

graph = defaultdict(list)

# 인접 리스트 구성
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 번호가 작은 것부터 방문하기 위해 정렬
for key in graph:
    graph[key].sort()

# DFS
def dfs(start):
    stack = [start]
    visited = set()
    result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            # 작은 번호부터 방문하기 위해 reversed 사용
            stack.extend(reversed(graph[node]))
    return result

# BFS
def bfs(start):
    q = deque([start])
    visited = set([start])
    result = [start]

    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                result.append(neighbor)
                q.append(neighbor)
    return result

# 출력
print(' '.join(map(str, dfs(v))))
print(' '.join(map(str, bfs(v))))