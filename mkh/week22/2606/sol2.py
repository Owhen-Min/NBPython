from collections import defaultdict, deque

# BFS 방식

n = int(input())
e = int(input())

dd = defaultdict(list)

# 인접 그래프 갱신
for i in range(e):
    n1, n2 = map(int,input().split())
    dd[n1].append(n2)
    dd[n2].append(n1)

# 1을 통해 방문한 노드들을 기록할 방문배열 세트
visited = set()

# 1에서부터 시작한다.
queue = deque([1])

while queue:
    # 갈 수 있는 곳을 뽑아서
    curr = queue.popleft()
    # 방문한 적이 없다면
    if curr not in visited:
        # 방문 표시를 하고 해당 노드에서 갈 수 있는 곳들을 추가한다.
        visited.add(curr)
        queue.extend(dd[curr])

print(len(visited)-1)
