n, m = map(int,input().split())
ts = list(map(int,input().split()))
curr = 1
ans = 0
for i in range(m):
    # 왼쪽으로 돌아가서 타겟 숫자로 뽑는 경우, 오른쪽으로 돌아가서 타겟 숫자를 뽑는 경우 중 짧은 길로 가기
    ans += min(abs(ts[i]-curr), n+min(curr, ts[i])-max(curr, ts[i]))
    # 현재 위치를 갱신한다.
    curr = ts[i]
    # 전체 길이가 줄어든다.
    n -= 1
    # 전체의 길이가 줄었으므로 뒤에 있던 애들은 한칸씩 땡긴다.
    ts = list(x-1 if x > ts[i] else x for x in ts)

print(ans)