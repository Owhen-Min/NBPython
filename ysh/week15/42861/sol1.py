from collections import deque

def solution(n, costs):
    # 최소비용을 담을 변수
    answer = 0
    # 빈 인접리스트 생성
    adj_list = [[] for _ in range(n)]
    # 인접리스트 만들기
    for s, e, cost in costs:
        adj_list[s].append([e, cost])
        adj_list[e].append([s, cost])
        # 초기값을 적당한 큰 숫자로 하기위해 모든 다리의 비용을 합산
        answer += cost
    # 모든 섬에서 BFS탐색 시작
    for start in range(n):
        # 시작할 섬의 번호 / 사용한 비용 / 방문기록 을 할당
        queue = deque([[start, 0, [0] * n]])
        while queue:
            # 지금 와있는 섬을 갱신
            pre_node, pre_cost, visited = queue.popleft()
            # 방문기록
            visited = visited.copy()
            visited[pre_node] = 1
            # 현재까지의 비용이 이미 최소값보다 커졌다면?
            # 더이상 계산할 필요가 없음
            if pre_cost > answer:
                continue
            # 모든 섬을 방문 했다면?
            if sum(visited) == n:
                # 최소값을 갱신할 수 있다면?
                if pre_cost < answer:
                    answer = pre_cost
                continue
            # 현재 섬에서 갈 수 있는 다른 섬들을 비용과 방문기록을 같이 넣기
            for next_node, cost in adj_list[pre_node]:
                # 방문한 섬이라면 무시
                if visited[next_node]:
                    continue
                queue.append([next_node, pre_cost + cost, visited])

    return answer

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))