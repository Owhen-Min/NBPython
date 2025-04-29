# 그래프 -> 인접리스트를 사용하면 되겠구나~

from collections import deque

def min_steps(a, b, n, pairs):
    graph = [[] for _ in range(n + 1)] # 그래프
    
    # 인접 리스트
    for x, y in pairs:
        graph[x].append(y)
        graph[y].append(x)
   
    # 큐, 방문 설정
    queue = deque()
    visited = [False] * (n + 1)
    
    # 시작점
    queue.append((a, 0))  # (현재 문자, 횟수)
    visited[a] = True
    
    while queue:
        current, steps = queue.popleft()
        
        if current == b:
            return steps
        
        for i in graph[current]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, steps + 1))
    
    # b에 도달할 수 없으면 -1
    return -1

a, b = map(int, input().split())
n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

print(min_steps(a, b, n, pairs))
