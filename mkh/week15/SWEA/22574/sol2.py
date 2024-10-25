T = int(input())
NMs = [list(map(int,input().split())) for _ in range(T)]
mx = max([x[0] for x in NMs])
ls = [1] * (mx+1)
ans = ''
for i in range(2,mx+1):
    ls[i] = ls[i-1]+i
for _ in range(T):
    n, m = NMs[_]
    if m in ls[:n+1]:
        ans += str(ls[n]-1)+'\n'
    else:
        ans += str(ls[n]) + '\n'
print(ans)