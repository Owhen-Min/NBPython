from collections import defaultdict, deque

a, b = map(int,input().split())
n, m = map(int,input().split())
# 인접리스트 생성
dd = defaultdict(set)

for _ in range(m):
    n1, n2 = map(int,input().split())
    dd[n1].add(n2)
    dd[n2].add(n1)

# BFS 시작
q = deque([(a,0)])
# 백트래킹을 위한 visited 배열
visited = set()
ans = -1

while q:
    curr, cost = q.popleft()
    if curr == b:
        ans = cost
        break
    # 다음 배열을 한번에 q에 추가하고 (단 이전에 방문했거나 방문할 예정이면 또 탐색할 필요 없으니 쳐내기)
    q.extend(((next, cost+1) for next in dd[curr] if next not in visited) )
    # 이미 갈거라고 예약해뒀으니까 visited에 넣고 관리하기.
    visited.update(dd[curr])

print(ans)