from itertools import combinations
from functools import reduce

n = int(input()) 
ingreds = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

for r in range(1, n + 1):  # 크기가 1부터 n까지의 모든 부분 집합을 탐색
    for comb in combinations(ingreds, r):
        sour, bitter = reduce(lambda x, y: (x[0] * y[0], x[1] + y[1]), comb, (1, 0))
        ans = min(ans, abs(sour - bitter))

print(ans)