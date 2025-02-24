n = int(input())
ingreds = [list(map(int,input().split())) for _ in range(n)]
subsets = [[1, 0]]
ans = 10e9

# append로 구하는 모든 부분 집합의 수 방식
for s, b in ingreds:
    temp = []
    for so, bi in subsets:
        temp.append([so*s, bi+b])
    subsets.extend(temp)

for i in range(1, len(subsets)):
    sour, bitter = subsets[i]
    ans = min(ans, abs(sour-bitter))

print(ans)