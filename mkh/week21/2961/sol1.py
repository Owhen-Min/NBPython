from itertools import combinations

n = int(input())
ingreds = [list(map(int,input().split())) for _ in range(n)]
ans = 10e9
# 재료들의 최고의 조합을 찾기 위해 모든 조합 구하기.
for i in range(1, n+1):
    posses = combinations(ingreds, i)
    for poss in posses:
        sour = 1
        bitter = 0
        for s, b in poss:
            sour *= s
            bitter += b
        if ans > abs(sour-bitter):
            ans = abs(sour-bitter)

print(ans)
