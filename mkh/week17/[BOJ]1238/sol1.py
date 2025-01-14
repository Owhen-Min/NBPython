from collections import deque
'''
전형적인 다익스트라 문제.
x번 마을로 도착하는 거리와 x번 마을에서 돌아가는 거리를 나누어서
두번 다익스트라 알고리즘을 적용해야 풀 수 있다.
따라서 순방향, 역방향 인접리스트를 두개 만들어서
각각 다익스트라 알고리즘을 적용한다.
'''

# 다익스트라를 적용하는 함수
def djk(adjl, costl):
    q = deque([x])
    costl[x] = 0
    while q:
        cur = q.popleft()
        for nxt, c in adjl[cur]:
            if costl[nxt] > costl[cur] + c:
                costl[nxt] = costl[cur] + c
                q.append(nxt)
    return costl

n, m, x = map(int, input().split())
# 순방향 인접리스트와 역방향 인접리스트를 담을 리스트
adjl = [[] for _ in range(n+1)]
rev_adjl = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    adjl[a].append((b, c))
    rev_adjl[b].append((a, c))

costl = [10e9] * (n+1)
rev_costl = [10e9] * (n+1)

costl = djk(adjl, costl)
rev_costl = djk(rev_adjl, rev_costl)

print(max(costl[x] + rev_costl[x] for x in range(1, n+1)))