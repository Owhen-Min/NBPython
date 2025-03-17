a, k = map(int,input().split())
ans = 0
while a != k:
    if k %2:
        ans += 1
        k -= 1
    elif k >= a*2:
        k /=2
        ans += 1
    else:
        k -= 1
        ans += 1

print(ans)

