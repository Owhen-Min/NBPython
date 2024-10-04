T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ls = list(map(int, input().split()))
    ans = round(sum(ls)/N,20)
    if ans == int(ans): ans = int(ans)
    print(f'#{tc} {ans}')