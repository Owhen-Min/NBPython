import heapq


# 프림 알고리즘
def solution(n, costs):
    # 모든 섬들이 연결되어 있으므로 최소힙으로 접근할 경우 내가 갈 수 있는 곳 중에서 최소 비용이고, 안 가본 곳으로만 가면 최적값이 나온다.
    # 따라서 최적값으로 탐색을 한번만 해도 충분.
    adjl = [[] for _ in range(n)]
    for cost in costs:
        s, e, c = cost
        adjl[s].append((c, e))
        adjl[e].append((c, s))
    # 인접 리스트 만들기.
    # 양방향이므로 각각의 위치에 갈 수 있는 곳과 값을 저장한다. 힙을 쓰기 위해 cost를 앞에 배치해둔다.
    visited = [False] * n
    # visited를 Boolean으로 관리한다.
    min_heap = [(0, 0)]
    # 모든 섬이 연결되어 있으므로 항상 0에서 시작해도 문제 없다. 0번 섬에서 시작하는 cost는 0
    min_cost = 0
    # 한번만 탐색하면 되므로 min_cost는 항상 더해간 결과값을 더해가서 한번만 구한다.
    visited_nodes = 0
    # visited를 순회하면서 False가 없는지를 확인하는 것은 번거로우므로 depth를 하나 들어갈 때마다 +1로 해서 n이 될때까지 탐색
    while visited_nodes != n:
        # 방문한 노드들이 n개면(모두 돌았다면) 탐색을 중단한다.
        cost, node = heapq.heappop(min_heap)
        # 내가 방문할 수 있는 노드 중에 가장 비용이 적은 노드를 뽑아서 확인한다.
        if visited[node]:
            continue
        # 담을 때는 방문하지 않았지만 뽑아봤더니 방문한 곳이라면, 다른 가능성을 탐색한다.
        visited[node] = True
        visited_nodes += 1
        min_cost += cost
        # visited를 갱신하고, 방문한 노드의 수를 업데이트한다.

        for n_cost, n_node in adjl[node]:
            if not visited[n_node]:
                heapq.heappush(min_heap, (n_cost, n_node))
        # 방문하지 않은 노드들을 힙에 집어넣고 다음에 추가할 수 있게 갱신한다.

    return min_cost