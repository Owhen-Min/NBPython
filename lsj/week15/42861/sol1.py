from collections import defaultdict  # 기본 값을 가지는 딕셔너리 생성
import heapq  # 최소 힙(Min Heap)을 사용하기 위한 모듈

def solution(n, costs):
    graph = defaultdict(list)  # 인접 리스트로 그래프 표현

    # 그래프를 인접 리스트 형태로 구성
    for srt, dst, weight in costs:
        graph[srt].append((dst, weight))  # 시작 정점 -> 도착 정점 (가중치)
        graph[dst].append((srt, weight))  # 도착 정점 -> 시작 정점 (가중치) (양방향 그래프)

    # 최소 신장 트리(MST) 구성을 위한 행렬과 초기화된 노드 정보
    mst_graph = [[0] * n for _ in range(n)]  # MST 인접 행렬 초기화
    mst_nodes = [-1 for _ in range(n)]  # 각 노드의 가중치 저장
    visited = [True for _ in range(n)]  # 노드 방문 여부를 추적하는 리스트

    # 우선순위 큐를 사용하여 (가중치, 현재 노드, 이전 노드) 형태로 저장
    q = [(0, 1, 1)]  # (초기 가중치, 시작 정점, 이전 정점)

    # 우선순위 큐를 이용해 프림 알고리즘 수행
    while q:
        cost, node, prev = heapq.heappop(q)  # 최소 가중치 간선 선택

        # 이미 방문한 노드는 건너뜀
        if visited[node - 1] is False:
            continue

        visited[node - 1] = False  # 현재 노드를 방문 처리

        # MST에 포함된 간선을 인접 행렬에 표시
        mst_graph[node - 1][prev - 1] = 1
        mst_graph[prev - 1][node - 1] = 1

        # 현재 노드의 최소 가중치를 저장
        mst_nodes[node - 1] = cost

        # 현재 노드와 연결된 인접 노드들을 큐에 추가
        for dst, weight in graph[node]:
            if visited[dst - 1] is True:  # 방문하지 않은 노드만 추가
                heapq.heappush(q, (weight, dst, node))


    answer = sum(mst_nodes)
    return answer