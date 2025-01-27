from itertools import combinations

n, s = map(int,input().split())
ls = list(map(int,input().split()))
ans = 0

# 들어가는 숫자의 갯수를 정해서
for i in range(1, n+1):
    # i개 고른 조합을 만든 후에
    combis = combinations(ls, i)
    for combi in combis:
        # 그 합이 s라면 ans에 + 1
        if sum(combi) == s:
            ans += 1

print(ans)