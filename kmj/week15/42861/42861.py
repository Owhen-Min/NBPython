# 현재까지 연결된 노드에서 최소 비용으로 새로운 노드 추가
# 우선순위큐를 사용해서 최소 비용 찾기 -> 방문하지 않은 곳이면 비용 추가 -> 다음 방문할 곳 찾기

# [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]] # [u,v,coat]..노드1,노드2,비용
import heapq

def solution(n, costs):
    # 인접 리스트
    graph = [[] for _ in range(n)]
    for u, v, cost in costs:
        graph[u].append((cost, v))
        graph[v].append((cost, u))

    visited = [False] * n  # 각 노드의 방문 여부
    min_heap = [(0, 0)]  # (비용, 노드) 초기화
    total_cost = 0  # 최소 비용 저장

    while min_heap:
        cost, node = heapq.heappop(min_heap)  # 가장 작은 비용의 노드 선택

        if visited[node]:
            continue  # 이미 방문한 노드라면 무시하고 다음 최소힙 pop하러 go

        visited[node] = True  # 노드를 방문으로 표시
        total_cost += cost  # 현재 노드의 비용 추가

        # 다음 방문할 곳 비용, 다음 방문할 노드
        for nx_cost, nx_node in graph[node]:
            if not visited[nx_node]:  # 아직 방문하지 않은 노드만 추가
                heapq.heappush(min_heap, (nx_cost, nx_node))

    return total_cost
